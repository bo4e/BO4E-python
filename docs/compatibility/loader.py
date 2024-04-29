"""
Contains functions to load and save schema files and changes
"""

import json
from pathlib import Path
from typing import Iterable

from bost.schema import SchemaRootType
from pydantic import TypeAdapter

from . import change_schemas


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
