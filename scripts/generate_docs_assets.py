"""Generate documentation assets that Sphinx consumes:

- ``docs/_static/images/bo4e/<pkg>/<Class>.svg``  (per-class diagrams)
- ``docs/_static/tables/compatibility_matrix.csv``
- ``docs/_static/tables/changes_table.csv``
- ``docs/_static/tables/changes/<old>_to_<new>.json``

Prereqs:
    - ``bo4e`` binary on PATH (see ``.github/actions/setup-bo4e`` for CI).
    - kroki reachable at ``$KROKI_URL`` (default ``http://localhost:8000``;
      see ``docker-compose.yml``).
    - ``json_schemas/`` populated for the current version (``tox -e
      generate_json_schemas`` first; ``tox -e docs`` does this).

Caching: pulled schemas land in ``tmp/bo4e_json_schemas/<tag>/``. The
script skips ``bo4e pull`` when that directory already exists — for the
local-dev iterative loop. CI runners are fresh and always re-pull.

Env overrides:
    - ``BO4E_DOCS_REF``    reference for ``bo4e repo versions`` (default
                           ``HEAD``; the release workflow sets the tag).
    - ``BO4E_DOCS_LABEL``  user-facing label for the current json_schemas/
                           source. Appears in SVG cross-link URLs, in the
                           matrix's "current" column, and in
                           changes_table.csv / diff filenames. Workflows
                           that deploy under a stable routing path
                           override this so artefacts match the deploy URL
                           (``latest``, ``test-XXXXXX``, or the release
                           tag). When unset, it defaults to
                           ``bo4e.__gh_version__``.
    - ``KROKI_URL``        kroki endpoint for the PlantUML → SVG step.
"""

from __future__ import annotations

import csv
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import bo4e

# Make our own prints line-buffered so they interleave naturally with the
# inherited stdout from bo4e subprocesses. Without this, tox sees a non-TTY
# stdout and Python fully buffers print() calls, making the log appear out
# of order against the subprocesses (which write to the same handle but
# without Python's buffer).
sys.stdout.reconfigure(line_buffering=True)  # type: ignore[union-attr]

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_SCHEMAS_DIR = REPO_ROOT / "json_schemas"
SCHEMAS_CACHE = REPO_ROOT / "tmp/bo4e_json_schemas"
IMG_OUT = REPO_ROOT / "docs/_static/images/bo4e"
TABLES_OUT = REPO_ROOT / "docs/_static/tables"
CHANGES_OUT = TABLES_OUT / "changes"

REF = os.environ.get("BO4E_DOCS_REF", "HEAD")
KROKI_URL = os.environ.get("KROKI_URL", "http://localhost:8000")
KROKI_CONCURRENCY = int(os.environ.get("KROKI_CONCURRENCY", "8"))
DOCS_LABEL_OVERRIDE = os.environ.get("BO4E_DOCS_LABEL")

# bo4e CLI reads only GITHUB_ACCESS_TOKEN. GitHub Actions auto-injects
# GITHUB_TOKEN. Alias one to the other so the workflow doesn't have to set
# both. Without authentication, bo4e pull burns through GitHub's 60 req/hr
# anonymous limit within a single pull (192 schema files).
if not os.environ.get("GITHUB_ACCESS_TOKEN") and os.environ.get("GITHUB_TOKEN"):
    os.environ["GITHUB_ACCESS_TOKEN"] = os.environ["GITHUB_TOKEN"]

# Mirrors bo4e-cli's REGEX_DIRTY_VERSION dirty-tail.
_DIRTY_RE = re.compile(r"\+g[0-9a-f]+|\.d[0-9]{8}")
# Last "↦ <version>" segment on the matrix header line.
_MATRIX_LAST_COL_RE = re.compile(r"↦ [^,↦]*$")
# Mirrors bo4e-cli v1.1.1's is_valid_github_token regex
# (crates/bo4e-cli/src/io/github.rs). Used to diagnose token format issues
# before invoking the CLI.
_BO4E_TOKEN_RE = re.compile(
    r"^(gh[pousr]_[A-Za-z0-9_]{36,}" r"|github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}" r"|v[0-9]\.[0-9a-f]{40})$"
)


def _format_cmd(args: tuple[str | os.PathLike[str], ...]) -> str:
    """Render a command for log output. Strings only — no real shell quoting needed."""
    return " ".join(str(a) for a in args)


def _run_with_pty(cmd: list[str]) -> int:
    """Run cmd attached to a pseudo-TTY and stream its output. POSIX only.

    A real PTY makes TUI-style subprocess output (indicatif-style progress
    bars from bo4e pull, for example) render normally — without it, the
    subprocess detects a non-TTY stdout and falls back to silence during the
    long-running download phase. Returns the subprocess exit code.
    """
    import fcntl
    import pty
    import select
    import struct
    import termios

    master, slave = pty.openpty()
    try:
        size = shutil.get_terminal_size((24, 80))
        fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack("HHHH", size.lines, size.columns, 0, 0))
    except (OSError, ValueError):
        pass

    proc = subprocess.Popen(cmd, stdin=slave, stdout=slave, stderr=slave, close_fds=True)
    os.close(slave)
    try:
        while True:
            try:
                ready, _, _ = select.select([master], [], [], 0.1)
            except (OSError, ValueError):
                break
            if master in ready:
                try:
                    data = os.read(master, 4096)
                except OSError:
                    break
                if not data:
                    break
                sys.stdout.buffer.write(data)
                sys.stdout.buffer.flush()
            elif proc.poll() is not None:
                break
        return proc.wait()
    finally:
        os.close(master)


def run(*args: str | os.PathLike[str]) -> None:
    """Run a subprocess with live output and abort on failure.

    On POSIX we attach a pseudo-TTY so progress-bar output (e.g. bo4e pull's
    download progress) renders. On Windows we fall back to plain
    stdout/stderr inheritance — Python's stdlib has no portable PTY, so TUI
    output that requires isatty() won't render there.
    """
    print(f"$ {_format_cmd(args)}")
    cmd = [str(a) for a in args]
    if sys.platform != "win32":
        try:
            retcode = _run_with_pty(cmd)
        except OSError:
            # PTY allocation failed (containerised env without /dev/ptmx, etc.).
            # Fall back to plain inheritance.
            subprocess.run(cmd, check=True)
            return
    else:
        retcode = subprocess.run(cmd).returncode
    if retcode != 0:
        raise subprocess.CalledProcessError(retcode, cmd)


def run_stdout(*args: str | os.PathLike[str]) -> str:
    """Run a subprocess; stream stdout live and return it for parsing.

    Unlike ``subprocess.run(capture_output=True)`` — which buffers everything in
    memory and only returns once the process exits — this reads stdout line by
    line, mirrors each line to our own stdout so the user sees progress as it
    happens, and accumulates the captured text for callers that need to parse it.
    stderr is inherited (also live).
    """
    print(f"$ {_format_cmd(args)}")
    cmd = [str(a) for a in args]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True) as proc:
        assert proc.stdout is not None
        chunks: list[str] = []
        for line in proc.stdout:
            sys.stdout.write(line)
            chunks.append(line)
        retcode = proc.wait()
    if retcode != 0:
        raise subprocess.CalledProcessError(retcode, cmd)
    return "".join(chunks)


def version_str(version_obj: dict) -> str:
    """Reconstruct ``v<major>.<functional>.<technical>[-rc<n>][+g<commit>][.d<date>]``."""
    s = f"v{version_obj['major']}.{version_obj['functional']}.{version_obj['technical']}"
    if version_obj.get("candidate") is not None:
        s += f"-rc{version_obj['candidate']}"
    if version_obj.get("commit_part"):
        s += f"+g{version_obj['commit_part']}"
    date = version_obj.get("dirty_worktree_date")
    if date:
        s += f".d{date.replace('-', '')}"
    return s


def kroki_render(puml_path: Path, svg_path: Path) -> None:
    """POST a PlantUML source to kroki and write the returned SVG to disk."""
    body = json.dumps(
        {
            "diagram_source": puml_path.read_text(encoding="utf-8"),
            "diagram_type": "plantuml",
            "output_format": "svg",
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        KROKI_URL,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        svg_path.write_bytes(resp.read())


def render_diagrams(link_template: str, tmp: Path) -> None:
    """Run ``bo4e graph extract`` + ``single`` then push each PUML to kroki."""
    graph_json = tmp / "graph.json"
    run("bo4e", "graph", "extract", "-i", JSON_SCHEMAS_DIR, "-o", graph_json)

    uml_dir = tmp / "uml"
    run(
        "bo4e",
        "graph",
        "single",
        "-i",
        graph_json,
        "-o",
        uml_dir,
        "--class",
        "all",
        "--format",
        "plantuml",
        "--detail-root",
        "full",
        "--detail-neighbours",
        "none",
        "--clustering",
        "package",
        "--link-template",
        link_template,
    )

    # Enums show up as small unhelpful diagrams (no fields, no relations).
    # We still let bo4e graph emit them as .puml above — the CLI doesn't
    # offer a per-package filter at single-class generation time — but
    # don't bother rendering them to SVG.
    all_puml = sorted(uml_dir.rglob("*.puml"))
    puml_files = [p for p in all_puml if p.relative_to(uml_dir).parts[0] != "enum"]
    skipped = len(all_puml) - len(puml_files)
    total = len(puml_files)
    print(
        f"[kroki] rendering {total} diagrams via {KROKI_URL} "
        f"(pool size = {KROKI_CONCURRENCY}, skipped {skipped} enum puml files)"
    )
    # Pre-create the per-package output directories on the main thread so
    # workers don't race to mkdir the same path.
    pairs: list[tuple[Path, Path]] = []
    for puml in puml_files:
        rel = puml.relative_to(uml_dir)
        svg = IMG_OUT / rel.with_suffix(".svg")
        svg.parent.mkdir(parents=True, exist_ok=True)
        pairs.append((puml, svg))

    completed = 0
    with ThreadPoolExecutor(max_workers=KROKI_CONCURRENCY) as pool:
        futures = {pool.submit(kroki_render, puml, svg): svg.relative_to(IMG_OUT) for puml, svg in pairs}
        for future in as_completed(futures):
            future.result()  # re-raises on failure; cancels remaining via with-exit
            completed += 1
            print(f"[kroki] ({completed}/{total}) {futures[future]}")
    print(f"[graph] wrote SVGs to {IMG_OUT.relative_to(REPO_ROOT)}/")


def fetch_reference_versions() -> list[str]:
    """Return the last 3 release tags (excluding rcs / technical bumps)."""
    output = run_stdout("bo4e", "repo", "versions", "-q", "-c", "-t", "-n", "3", "-r", REF)
    return output.split()


def populate_schema_cache(tags: list[str]) -> None:
    """Pull each tag's schemas into ``SCHEMAS_CACHE``; skip ones already cached."""
    for tag in tags:
        cache_dir = SCHEMAS_CACHE / tag
        if cache_dir.is_dir():
            print(f"[pull] cache hit  {tag}")
        else:
            print(f"[pull] fetching   {tag}")
            run("bo4e", "pull", "-t", tag, "-o", cache_dir)
            print(f"[pull] done       {tag}")


def generate_pairwise_diffs(tags: list[str], tmp: Path) -> list[Path]:
    """Run ``bo4e diff schemas`` for each consecutive pair in the version chain.

    The chain is ``[json_schemas, tags[0], tags[1], ...]`` (newest first).
    Filenames are canonical ``<old>_to_<new>.json``; for the current-tree pair
    the "new" side uses ``BO4E_DOCS_LABEL`` when set (so deploy artefacts say
    ``latest`` rather than the underlying dirty version).
    """
    chain: list[Path | str] = [JSON_SCHEMAS_DIR] + [SCHEMAS_CACHE / t for t in tags]
    diff_dir = tmp / "diff"
    diff_dir.mkdir()

    diff_files: list[Path] = []
    for i in range(len(chain) - 1):
        new = chain[i]
        old = chain[i + 1]
        raw = diff_dir / f".raw_{i}.json"
        run("bo4e", "diff", "schemas", old, new, "-o", raw)

        data = json.loads(raw.read_text(encoding="utf-8"))
        old_ver = version_str(data["oldSchemas"]["version"])
        if i == 0 and DOCS_LABEL_OVERRIDE:
            new_ver = DOCS_LABEL_OVERRIDE
        else:
            new_ver = version_str(data["newSchemas"]["version"])

        final = diff_dir / f"{old_ver}_to_{new_ver}.json"
        raw.rename(final)
        diff_files.append(final)

    return diff_files


def build_matrix(diff_files: list[Path], tmp: Path, docs_label: str) -> None:
    """Write ``compatibility_matrix.csv``, relabelling the last column if needed.

    ``bo4e diff matrix`` v1.1.1 errors with "Node already exists with different
    attributes" when consecutive diffs share a version that added new schemas
    (the newly-added schemas have ``schema: null`` in the diff where they first
    appear but have full content in the next one, making the same version-node
    look inconsistent). Workaround: strip the schema bodies from temp copies
    before feeding the matrix command. The matrix only needs version metadata
    and the changes list, not the full schema content.
    """
    stripped_dir = tmp / "diff_stripped"
    stripped_dir.mkdir()

    stripped_files: list[Path] = []
    for f in diff_files:
        data = json.loads(f.read_text(encoding="utf-8"))
        for side in ("oldSchemas", "newSchemas"):
            for entry in data[side].get("schemas", []):
                entry.pop("schema", None)
        sf = stripped_dir / f.name
        sf.write_text(json.dumps(data), encoding="utf-8")
        stripped_files.append(sf)

    matrix_csv = TABLES_OUT / "compatibility_matrix.csv"
    run(
        "bo4e",
        "diff",
        "matrix",
        "-o",
        matrix_csv,
        "--use-emotes",
        *stripped_files,
    )
    print(f"[diff] wrote {matrix_csv.relative_to(REPO_ROOT)}")

    if DOCS_LABEL_OVERRIDE:
        # bo4e diff matrix builds column headers from .newSchemas.version, which we
        # can't override at generation time. Rewrite the last "↦ <version>" on the
        # header row only.
        lines = matrix_csv.read_text(encoding="utf-8").splitlines(keepends=True)
        if lines:
            stripped = lines[0].rstrip("\r\n")
            relabeled = _MATRIX_LAST_COL_RE.sub(f"↦ {docs_label}", stripped)
            ending = lines[0][len(stripped) :]
            lines[0] = relabeled + ending
            matrix_csv.write_text("".join(lines), encoding="utf-8")
        print(f"[diff] relabelled matrix last column to: {docs_label}")


def emit_changes_table(diff_files: list[Path]) -> None:
    """Copy each diff JSON into ``_static/tables/changes/`` and write ``changes_table.csv``."""
    for old in CHANGES_OUT.glob("*.json"):
        old.unlink()

    changes_table = TABLES_OUT / "changes_table.csv"
    with changes_table.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["Old Version", "New Version", "Diff-file"])
        for i, df in enumerate(diff_files):
            data = json.loads(df.read_text(encoding="utf-8"))
            old_ver = version_str(data["oldSchemas"]["version"])
            if i == 0 and DOCS_LABEL_OVERRIDE:
                new_ver = DOCS_LABEL_OVERRIDE
            else:
                new_ver = version_str(data["newSchemas"]["version"])
            name = df.name
            shutil.copyfile(df, CHANGES_OUT / name)
            # The link target is resolved by Sphinx relative to the document
            # that includes the CSV (docs/changelog.rst), NOT to the CSV file
            # itself. So the path needs the full docs-relative prefix
            # `_static/tables/changes/<name>`, not `changes/<name>`.
            link = f"_static/tables/changes/{name}"
            writer.writerow([old_ver, new_ver, f"`{name} <{link}>`__"])
    print(f"[diff] wrote {changes_table.relative_to(REPO_ROOT)}")


def main() -> int:
    if not shutil.which("bo4e"):
        sys.stderr.write("ERROR: 'bo4e' not on PATH. Install via setup-bo4e action or your package manager.\n")
        return 1

    # Diagnostics — useful when CI fails surprisingly. Never print the token
    # value. The length and prefix are not unique to any single secret and
    # therefore aren't masked by GitHub Actions' log scrubber.
    def _describe(env_name: str) -> str:
        value = os.environ.get(env_name, "")
        if not value:
            return f"{env_name}=unset"
        prefix = value[:4]
        bo4e_valid = bool(_BO4E_TOKEN_RE.match(value))
        return f"{env_name}=set (len={len(value)}, prefix={prefix!r}, " f"bo4e-regex-valid={bo4e_valid})"

    print(f"[auth] {_describe('GITHUB_ACCESS_TOKEN')}")
    print(f"[auth] {_describe('GITHUB_TOKEN')}")
    has_access_token = bool(os.environ.get("GITHUB_ACCESS_TOKEN"))
    has_github_token = bool(os.environ.get("GITHUB_TOKEN"))
    if not has_access_token and not has_github_token:
        print(
            "[auth] WARNING: no GitHub token in env. bo4e pull will fall back "
            "to anonymous requests and likely hit GitHub's 60 req/hr rate "
            "limit on the 192-schema fetch.",
            file=sys.stderr,
        )

    gh_version = bo4e.__gh_version__
    is_dirty = bool(_DIRTY_RE.search(gh_version))
    docs_label = DOCS_LABEL_OVERRIDE or gh_version

    if DOCS_LABEL_OVERRIDE or not is_dirty:
        link_template = f"https://bo4e.github.io/BO4E-python/{docs_label}/api/{{module}}.html"
    else:
        link_template = f"file://{REPO_ROOT.as_posix()}/.tox/docs/tmp/html/api/{{module}}.html"

    print(f"[graph] docs label:    {docs_label}")
    print(f"[graph] link template: {link_template}")

    for d in (IMG_OUT, TABLES_OUT, CHANGES_OUT, SCHEMAS_CACHE):
        d.mkdir(parents=True, exist_ok=True)

    tmp = Path(tempfile.mkdtemp(prefix="bo4e-docs-"))
    print(f"[setup] temp dir: {tmp}")
    try:
        render_diagrams(link_template, tmp)

        tags = fetch_reference_versions()
        print(f"[diff] reference versions: {tags}")
        populate_schema_cache(tags)

        diff_files = generate_pairwise_diffs(tags, tmp)
        build_matrix(diff_files, tmp, docs_label)
        emit_changes_table(diff_files)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print(f"[cleanup] removed temp dir: {tmp}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
