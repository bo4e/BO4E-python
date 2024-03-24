import json
from pathlib import Path
from typing import Iterable

import change_schemas
from bost.schema import SchemaRootType
from pydantic import TypeAdapter


def load_schema_file(path: Path) -> SchemaRootType:
    """
    Load a schema file and return the parsed schema
    """
    type_adapter = TypeAdapter(SchemaRootType)
    return type_adapter.validate_json(path.read_text("utf-8"))


def load_changes(path: Path) -> list[change_schemas.Change]:
    """
    Load a changes file and return the parsed changes
    """
    type_adapter = TypeAdapter(list[change_schemas.Change])
    return type_adapter.validate_json(path.read_text("utf-8"))


def save_changes(path: Path, changes: Iterable[change_schemas.Change]):
    """
    Save the changes to a file
    """
    json.dump(
        TypeAdapter(list[change_schemas.Change]).dump_python(list(changes), mode="json"),
        open(path, "w", encoding="utf-8"),
    )


def get_namespace(path: Path) -> Iterable[tuple[str, ...]]:
    """
    Get the namespace from a file
    """
    for schema_file in path.rglob("*.json"):
        sub_path = schema_file.relative_to(path).parts[:-1]
        yield *sub_path, schema_file.stem
