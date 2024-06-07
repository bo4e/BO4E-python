"""
Contains functions to load and save schema files and changes
"""

import json
import shutil
from pathlib import Path
from typing import Iterable

from bost import main as bost_main
from bost.operations import update_references as bost_update_references
from bost.pull import SchemaMetadata
from bost.schema import SchemaRootType
from pydantic import TypeAdapter

from . import change_schemas

BO4E_BASE_DIR = Path(__file__).parents[2] / "tmp/bo4e_json_schemas"
LOCAL_JSON_SCHEMA_DIR = Path(__file__).parents[2] / "json_schemas"


def load_schema_file(path: Path) -> SchemaRootType:
    """
    Load a schema file and return the parsed schema
    """
    return TypeAdapter(SchemaRootType).validate_json(path.read_text("utf-8"))  # type: ignore[return-value]
    # mypy has problems to infer the Union type here.


def load_changes(path: Path) -> list[change_schemas.Change]:
    """
    Load a changes file and return the parsed changes
    """
    return TypeAdapter(list[change_schemas.Change]).validate_json(path.read_text("utf-8"))


def save_changes(path: Path, changes: Iterable[change_schemas.Change]) -> None:
    """
    Save the changes to a file
    """
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            TypeAdapter(list[change_schemas.Change]).dump_python(list(changes), mode="json"),
            file,
        )


def get_namespace(path: Path) -> Iterable[tuple[str, ...]]:
    """
    Get the namespace from a file
    """
    for schema_file in path.rglob("*.json"):
        sub_path = schema_file.relative_to(path).parts[:-1]
        yield *sub_path, schema_file.stem


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
    for schema_path in get_namespace(path):
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
