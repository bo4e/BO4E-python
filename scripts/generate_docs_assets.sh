#!/usr/bin/env bash
# Generate documentation assets that Sphinx consumes:
#   - docs/_static/images/uml/<pkg>/<Class>.svg  (per-class diagrams)
#   - docs/_static/tables/compatibility_matrix.csv
#   - docs/_static/tables/changes_table.csv
#   - docs/_static/tables/changes/<old>_to_<new>.json
#
# Prereqs:
#   - bo4e binary on PATH (see .github/actions/setup-bo4e for CI)
#   - kroki reachable at http://localhost:8000 (see docker-compose.yml)
#   - json_schemas/ already populated for the *current* version (run
#     `tox -e generate_json_schemas` first; tox -e docs does this).
#
# Caching: schema pulls go into tmp/bo4e_json_schemas/<tag>/. The script
# skips bo4e pull when that directory already exists. This is intended for
# the local-dev iterative loop; CI runners are fresh and always re-pull.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

REF="${BO4E_DOCS_REF:-HEAD}"                  # repo-versions reference
SCHEMAS_CACHE="tmp/bo4e_json_schemas"          # local-dev cache
KROKI_URL="${KROKI_URL:-http://localhost:8000}"

# Resolve a Python interpreter that has the bo4e package importable.
# Priority: explicit $PYTHON env var > python/python3 on PATH that has bo4e >
#           uv run python3 (project venv fallback for standalone runs).
# Sets the global PYTHON_ARGS array so callers can do: "${PYTHON_ARGS[@]}" -c ...
PYTHON_ARGS=()
_find_python() {
    for cand in "${PYTHON:-}" python python3; do
        [ -z "${cand}" ] && continue
        if "${cand}" -c "import bo4e" 2>/dev/null; then
            PYTHON_ARGS=("${cand}")
            echo "[python] using: ${cand}"
            return
        fi
    done
    if command -v uv >/dev/null 2>&1; then
        if uv run python3 -c "import bo4e" 2>/dev/null; then
            PYTHON_ARGS=(uv run python3)
            echo "[python] using: uv run python3"
            return
        fi
    fi
    echo "ERROR: no Python interpreter with 'bo4e' found. Set PYTHON= or run inside the tox/uv env." >&2
    exit 1
}
_find_python

TMP="$(mktemp -d)"
trap 'rm -rf "${TMP}"' EXIT

IMG_OUT="docs/_static/images/uml"
TABLES_OUT="docs/_static/tables"
CHANGES_OUT="${TABLES_OUT}/changes"

mkdir -p "${IMG_OUT}" "${TABLES_OUT}" "${CHANGES_OUT}" "${SCHEMAS_CACHE}"

command -v bo4e >/dev/null 2>&1 || { echo "ERROR: 'bo4e' not on PATH. Install via setup-bo4e action or your package manager." >&2; exit 1; }
command -v jq   >/dev/null 2>&1 || { echo "ERROR: 'jq' is required." >&2; exit 1; }
command -v curl >/dev/null 2>&1 || { echo "ERROR: 'curl' is required." >&2; exit 1; }

# Reconstruct the canonical version string "v<major>.<functional>.<technical>[rc<n>][+g<commit>]"
# from the structured version object in a diff JSON file.
_version_str() {
    local file="$1" field="$2"
    jq -r "${field} | \
        \"v\" + (.major|tostring) + \".\" + (.functional|tostring) + \".\" + (.technical|tostring) + \
        if .candidate != null then \"rc\" + (.candidate|tostring) else \"\" end + \
        if .commit_part != null then \"+g\" + .commit_part else \"\" end" "${file}"
}

#############################################
# 1. Per-class UML diagrams
#############################################

GH_VERSION="$("${PYTHON_ARGS[@]}" -c 'import bo4e; print(bo4e.__gh_version__)')"
if printf '%s' "${GH_VERSION}" | grep -Eq '\+g[0-9a-f]+|\.d[0-9]{8}'; then
    LINK_TEMPLATE="file://${REPO_ROOT}/.tox/docs/tmp/html/api/{module}.html"
else
    LINK_TEMPLATE="https://bo4e.github.io/BO4E-python/${GH_VERSION}/api/{module}.html"
fi
echo "[graph] link template: ${LINK_TEMPLATE}"

bo4e graph extract -i json_schemas -o "${TMP}/graph.json"

bo4e graph single \
    -i "${TMP}/graph.json" \
    -o "${TMP}/uml" \
    --class all \
    --format plantuml \
    --detail-root full \
    --detail-neighbours none \
    --clustering package \
    --link-template "${LINK_TEMPLATE}"

# PlantUML -> SVG via locally hosted kroki.
find "${TMP}/uml" -name '*.puml' -print0 | while IFS= read -r -d '' puml; do
    rel="${puml#${TMP}/uml/}"
    svg="${IMG_OUT}/${rel%.puml}.svg"
    mkdir -p "$(dirname "${svg}")"
    jq -Rs '{diagram_source:.,diagram_type:"plantuml",output_format:"svg"}' < "${puml}" \
        | curl --fail --silent --show-error \
            -X POST -H 'Content-Type: application/json' \
            --data @- \
            "${KROKI_URL}" \
            -o "${svg}"
done
echo "[graph] wrote SVGs to ${IMG_OUT}/"

#############################################
# 2. Diff matrix + changes table
#############################################

# Last 3 release tags, descending. Empty if the repo has fewer than 3 tags
# matching the bo4e versioning scheme (won't happen in practice).
mapfile -t TAGS < <(bo4e repo versions -q -c -t -n 3 -r "${REF}")
echo "[diff] reference versions: ${TAGS[*]}"

for tag in "${TAGS[@]}"; do
    dir="${SCHEMAS_CACHE}/${tag}"
    if [ -d "${dir}" ]; then
        echo "[diff] cache hit  ${tag}"
    else
        echo "[diff] pulling   ${tag}"
        bo4e pull -t "${tag}" -o "${dir}"
    fi
done

# Build the chain: current json_schemas/ -> newest tag -> ... -> oldest tag
chain=("json_schemas")
for tag in "${TAGS[@]}"; do
    chain+=("${SCHEMAS_CACHE}/${tag}")
done

mkdir -p "${TMP}/diff" "${TMP}/diff_stripped"
diff_files=()
for i in $(seq 0 $((${#chain[@]} - 2))); do
    new="${chain[$i]}"
    old="${chain[$((i + 1))]}"
    raw="${TMP}/diff/.raw_${i}.json"
    bo4e diff schemas "${old}" "${new}" -o "${raw}"
    old_ver="$(_version_str "${raw}" '.oldSchemas.version')"
    new_ver="$(_version_str "${raw}" '.newSchemas.version')"
    final="${TMP}/diff/${old_ver}_to_${new_ver}.json"
    mv "${raw}" "${final}"
    diff_files+=("${final}")
done

# bo4e diff matrix (CLI v1.1.1) fails with "Node already exists with different
# attributes" when the same version appears on both sides of two consecutive
# diffs AND that version transition added new schemas (newly-added schemas have
# schema:null in the diff where they first appear but have full content in the
# next diff, making the node appear to have "different attributes").
# Workaround: strip the schema body from old/newSchemas before the matrix call.
# The matrix command only needs version metadata and the changes list.
stripped_diff_files=()
for f in "${diff_files[@]}"; do
    stripped="${TMP}/diff_stripped/$(basename "${f}")"
    jq 'del(.oldSchemas.schemas[].schema) | del(.newSchemas.schemas[].schema)' \
        "${f}" > "${stripped}"
    stripped_diff_files+=("${stripped}")
done

bo4e diff matrix \
    -o "${TABLES_OUT}/compatibility_matrix.csv" \
    --use-emotes \
    "${stripped_diff_files[@]}"
echo "[diff] wrote ${TABLES_OUT}/compatibility_matrix.csv"

# Copy the per-pair diff JSONs into _static and emit changes_table.csv.
# Version strings live at .oldSchemas.version / .newSchemas.version in the diff JSON.

rm -f "${CHANGES_OUT}"/*.json 2>/dev/null || true
{
    echo "Old Version,New Version,Diff-file"
    for f in "${diff_files[@]}"; do
        old="$(_version_str "${f}" '.oldSchemas.version')"
        new="$(_version_str "${f}" '.newSchemas.version')"
        name="$(basename "${f}")"
        cp "${f}" "${CHANGES_OUT}/${name}"
        printf '%s,%s,`%s <%s>`__\n' \
            "${old}" "${new}" "${name}" "changes/${name}"
    done
} > "${TABLES_OUT}/changes_table.csv"
echo "[diff] wrote ${TABLES_OUT}/changes_table.csv"
