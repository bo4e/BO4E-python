"""
This module provides functions to compare the BO4E JSON schemas of different versions.
It also contains functions to query GitHub for the latest BO4E versions to compare with the schemas of the current
work tree.
Additionally, it implements a little cache functionality to avoid multiple downloads of the same versions e.g.
if you're testing locally.
"""

import itertools
import logging
import re
import shutil
from pathlib import Path
from typing import Any as _Any
from typing import Iterable

import bost.operations
from bost import main as bost_main
from bost.operations import update_references as bost_update_references
from bost.pull import OWNER, REPO, SchemaMetadata, get_source_repo

from . import change_schemas, diff, loader, matrix

BO4E_BASE_DIR = Path(__file__).parents[2] / "tmp/bo4e_json_schemas"
LOCAL_JSON_SCHEMA_DIR = Path(__file__).parents[2] / "json_schemas"
logger = logging.getLogger(__name__)


def pull_bo4e_version(version: str, output: Path, gh_token: str | None = None) -> None:
    """
    Pull the BO4E version from the given version string.
    """
    bost_main(
        output=output,
        target_version=version,
        update_refs=True,
        set_default_version=False,
        clear_output=True,
        token=gh_token,
    )


def update_references(path: Path, version: str) -> None:
    """
    Update the references in the given path. This step is needed for the local build.
    """
    schema_namespace = {}
    for schema_path in loader.get_namespace(path):
        local_path = Path(path, *schema_path).with_suffix(".json")
        schema_namespace[schema_path[-1]] = SchemaMetadata(
            class_name=schema_path[-1],
            download_url="",
            module_path=schema_path,
            file_path=local_path,
            cached_path=local_path,
            token=None,
        )
    for schema_metadata in schema_namespace.values():
        bost_update_references(schema_metadata, schema_namespace, version)
        schema_metadata.save()


def pull_or_reuse_bo4e_version(version: str, gh_token: str | None = None, from_local: bool = False) -> Path:
    """
    Pull the BO4E version from the given version string or reuse the version if it was already pulled before.
    If version is None use the BO4E version of the checkout working directory by assuming the compiled json
    schemas in /json_schemas.
    Returns the path of the bo4e directory.
    """
    bo4e_dir = BO4E_BASE_DIR / version

    if from_local:
        if not any(LOCAL_JSON_SCHEMA_DIR.rglob("*.json")):
            raise ValueError(
                "No local json schemas found in /json_schemas. "
                "Please ensure that the json schemas are build on beforehand."
            )
        if bo4e_dir.exists():
            shutil.rmtree(bo4e_dir)
        shutil.copytree(LOCAL_JSON_SCHEMA_DIR, bo4e_dir)
        update_references(bo4e_dir, version)
    elif any(bo4e_dir.rglob("*.json")):
        return bo4e_dir
    else:
        pull_bo4e_version(version, bo4e_dir, gh_token)
    return bo4e_dir


def compare_bo4e_versions(
    version_old: str, version_new: str, gh_token: str | None = None, from_local: bool = False
) -> Iterable[change_schemas.Change]:
    """
    Compare the old version with the new version.
    If version_new is None use the BO4E version of the checkout working directory by assuming the compiled json
    schemas in /json_schemas.
    """
    dir_old_schemas = pull_or_reuse_bo4e_version(version_old, gh_token)
    dir_new_schemas = pull_or_reuse_bo4e_version(version_new, gh_token, from_local=from_local)
    print(f"Comparing {version_old} with {version_new}")
    yield from diff.diff_schemas(dir_old_schemas, dir_new_schemas)


def compare_bo4e_versions_iteratively(
    versions: Iterable[str], cur_version: str | None = None, gh_token: str | None = None
) -> dict[tuple[str, str], Iterable[change_schemas.Change]]:
    """
    Compare the versions iteratively. Each version at index i will be compared to the version at index i+1.
    Additionally, if cur_version is provided, the last version in the list will be compared to the version
    in the checkout working directory. The value of cur_version will be used to set the key in the returned
    dict.
    Note:
        - versions must contain at least one element.
        - versions should be sorted in ascending order.
        - if using cur_version, ensure that the json schemas of the checkout working directory
          were build on beforehand. They should be located in /json_schemas.
    """
    print(f"Comparing versions {versions} with cur_version {cur_version}")
    changes = {}
    last_version: str = ""  # This value is never used but makes mypy and pylint happy
    for version_old, version_new in itertools.pairwise(versions):
        last_version = version_new
        changes[version_old, version_new] = compare_bo4e_versions(version_old, version_new, gh_token)
    if cur_version is not None:
        changes[last_version, cur_version] = compare_bo4e_versions(last_version, cur_version, gh_token, from_local=True)
    print("Comparisons finished.")
    return changes


REGEX_RELEASE_VERSION = re.compile(r"^v(\d{6}\.\d+\.\d+)$")
REGEX_RELEASE_CANDIDATE_VERSION = re.compile(r"^v(\d{6}\.\d+\.\d+)-rc\d+$")


def get_last_n_release_versions(n: int, include_rc: bool = False, gh_token: str | None = None) -> Iterable[str]:
    """
    Get the last n release versions from the BO4E repository.
    """
    repo = get_source_repo(gh_token)
    releases = repo.get_releases()
    counter = 0

    for release in releases:
        if not REGEX_RELEASE_VERSION.fullmatch(release.tag_name) and (
            not include_rc or not REGEX_RELEASE_CANDIDATE_VERSION.fullmatch(release.tag_name)
        ):
            continue
        counter += 1
        yield release.tag_name
        if counter >= n:
            return

    logger.warning("Only %d matching releases found. Returning all releases.", counter)


def get_all_release_versions_since_20240100(include_rc: bool = False, gh_token: str | None = None) -> Iterable[str]:
    """
    Get all release versions since v202401.0.0 from the BO4E repository.
    """
    repo = get_source_repo(gh_token)
    releases = repo.get_releases()
    version_threshold = "v202401.0.0"

    for release in releases:
        if not REGEX_RELEASE_VERSION.fullmatch(release.tag_name) and (
            not include_rc or not REGEX_RELEASE_CANDIDATE_VERSION.fullmatch(release.tag_name)
        ):
            continue
        yield release.tag_name
        if release.tag_name == version_threshold:
            return

    logger.warning("Threshold version %s not found. Returned all matching releases.", version_threshold)


def _monkey_patch_bost_regex_if_local_testing(version: str) -> None:
    regex_expected_version = re.compile(r"^v\d+\.\d+\.\d+(?:-rc\d+)?$")
    if not regex_expected_version.fullmatch(version):
        bost.operations.REF_ONLINE_REGEX = re.compile(
            rf"^https://raw\.githubusercontent\.com/(?:{OWNER.upper()}|{OWNER.lower()}|Hochfrequenz)/{REPO}/"
            rf"(?P<version>[^/]+)/"
            r"src/bo4e_schemas/(?P<sub_path>(?:\w+/)*)(?P<model>\w+)\.json#?$"
        )


def create_tables_for_doc(
    compatibility_matrix_output_file: Path,
    gh_version: str,
    *,
    gh_token: str | None = None,
    last_n_versions: int = 2,
) -> None:
    """
    Creates the compatibility matrix for the documentation. The output is a csv file. This can be referenced
    inside Sphinx documentation. See https://sublime-and-sphinx-guide.readthedocs.io/en/latest/tables.html#csv-files
    for more information.
    If you have problems with rate limiting, please set gh_token.
    The compatibility matrix will be built for last_n_versions + the current version in the checkout working directory.
    If you set last_n_versions = 0 all versions since v202401.0.0 will be compared.
    Note: The matrix will never contain the first version as column. Each column is a comparison to the version before.
    Note: Release candidates are excluded.
    """
    _monkey_patch_bost_regex_if_local_testing(gh_version)
    logger.info("Retrieving the last %d release versions", last_n_versions)
    if last_n_versions > 0:
        versions = list(reversed(list(get_last_n_release_versions(last_n_versions, gh_token=gh_token))))
    else:
        versions = list(reversed(list(get_all_release_versions_since_20240100(gh_token=gh_token))))
    logger.info("Comparing versions iteratively: %s", " -> ".join([*versions, gh_version]))
    changes_iterables = compare_bo4e_versions_iteratively(versions, gh_version, gh_token=gh_token)
    logger.info("Building namespaces")
    changes = {key: list(value) for key, value in changes_iterables.items()}
    namespaces = {version: list(loader.get_namespace(BO4E_BASE_DIR / version)) for version in versions}
    namespaces[gh_version] = list(loader.get_namespace(BO4E_BASE_DIR / gh_version))
    logger.info("Creating compatibility matrix")
    matrix.create_compatibility_matrix_csv(
        compatibility_matrix_output_file, [*versions, gh_version], namespaces, changes
    )


def test_create_tables_for_doc() -> None:
    """
    Test the create_tables_for_doc function locally without building the entire documentation.
    Needs the JSON schemas to be present in /json_schemas with TARGET_VERSION set to "local".
    """
    create_tables_for_doc(
        Path(__file__).parents[1] / "compatibility_matrix.csv",
        "local",
        last_n_versions=3,
    )
