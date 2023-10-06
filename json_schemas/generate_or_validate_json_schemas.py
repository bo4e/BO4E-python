"""
This script is run in the tox 'json_schemas' environment.
"""

import importlib
import inspect
import json
import logging
import pkgutil
from pathlib import Path
from typing import Any, Literal, cast

import click
from pydantic import BaseModel

_logger = logging.getLogger(__name__)


def delete_json_schemas(packages: list[str]) -> None:
    """delete all json schemas"""
    for pkg in packages:
        for file in (Path(__file__).parent / pkg).iterdir():
            file.unlink()


def get_models(pkg: str) -> list[str]:
    """
    Get all models in a package
    """
    return [name for _, name, _ in pkgutil.iter_modules([str(Path(__file__).parent.parent / "src" / "bo4e" / pkg)])]


def get_classes(modl_name: str) -> list[tuple[str, type]]:
    """
    Get all classes in a module
    """
    modl = importlib.import_module(modl_name)
    return inspect.getmembers(modl, lambda member: inspect.isclass(member) and member.__module__ == modl_name)


def get_schema_json_dict(cls: type[BaseModel]) -> dict[str, Any]:
    """
    Get the json schema for a class
    """
    schema_json_dict = cls.model_json_schema()
    if "definitions" in schema_json_dict:
        for definition in schema_json_dict["definitions"].values():
            definition["description"] = definition["description"].strip()
    return schema_json_dict


def validate_schema(file_path: Path, schema_json_dict: dict[str, Any], name: str) -> None:
    """
    Validate the schema for a class
    """
    with open(file_path, "r", encoding="utf-8") as json_schema_file:
        existing_schema = json.load(json_schema_file)

    if schema_json_dict != existing_schema:
        raise ValueError(f"Schema for {name} has changed. Please run this script with mode 'generate'.")
        # or call tox -e generate_json_schemas
    _logger.debug("Schema for %s is consistent", name)


def generate_schema(file_path: Path, schema_json_dict: dict[str, Any], name: str) -> None:
    """
    Generate the schema for a class
    """
    with open(file_path, "w+", encoding="utf-8") as json_schema_file:
        json_schema_file.write(json.dumps(schema_json_dict, indent=4, sort_keys=True, ensure_ascii=False))
        json_schema_file.write("\n")
    _logger.debug("Generated schema for %s", name)


@click.command()
@click.option(
    "--mode",
    "-m",
    help="use 'validate' to validate existing schemas or 'generate' to generate new schemas",
    required=True,
    type=click.Choice(["validate", "generate"]),
)
def generate_or_validate_json_schemas(mode: Literal["validate", "generate"]) -> None:
    """generate json schemas for all BOs and COMs"""
    packages = ["bo", "com"]
    this_directory = Path(__file__).parent.absolute()

    if mode == "generate":
        delete_json_schemas(packages)

    for pkg in packages:
        modls = get_models(pkg)

        for model in modls:
            modl_name = f"bo4e.{pkg}.{model}"
            cls_list = get_classes(modl_name)

            for name, cls in cls_list:
                _logger.info("Processing %s", name)
                file_path = this_directory / pkg / (name + ".json")

                schema_json_dict = get_schema_json_dict(cast(type[BaseModel], cls))

                if mode == "validate":
                    validate_schema(file_path, schema_json_dict, name)
                elif mode == "generate":
                    generate_schema(file_path, schema_json_dict, name)
                else:
                    raise ValueError(f"Unknown mode '{mode}'")


if __name__ == "__main__":
    generate_or_validate_json_schemas()  # pylint:disable=no-value-for-parameter
