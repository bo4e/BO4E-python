"""
This script is run in the tox 'json_schemas' environment.
"""

import importlib
import inspect
import json
import logging
import pkgutil
import re
import sys
from enum import Enum
from pathlib import Path
from typing import Any, Iterator, Literal, cast

import click
from pydantic import BaseModel, TypeAdapter
from pydantic.json_schema import GenerateJsonSchema as _GenerateJsonSchema
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

from bo4e import ZusatzAttribut

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
_logger = logging.getLogger(__name__)
root_directory = Path(__file__).parent
output_directory = root_directory / "json_schemas"

NEW_REF_TEMPLATE = (
    "https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{version}/src/bo4e_schemas/{pkg}/{model}.json"
)
NEW_REF_TEMPLATE_ROOT = (
    "https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{version}/src/bo4e_schemas/{model}.json"
)
OLD_REF_TEMPLATE = re.compile(r"^#/\$defs/(?P<model>\w+)$")

PARSABLE_CLASS_TYPE = type[BaseModel] | type[Enum]


class GenerateJsonSchema(_GenerateJsonSchema):
    """
    This class is a copy of pydantic.json_schema.GenerateJsonSchema with the only difference that the
    decimal_schema method is overwritten to generate a JSON schema that can be used by the
    BO4E-Python-Generator (https://github.com/bo4e/BO4E-Python-Generator).
    """

    def decimal_schema(self, schema: core_schema.DecimalSchema) -> JsonSchemaValue:
        """
        Generates a JSON schema that matches a decimal value.
        The output format is changed to work well with BO4E-Python-Generator.
        """
        json_schema = self.str_schema(core_schema.str_schema())
        if self.mode == "validation":
            json_schema["format"] = "decimal"
        return json_schema


def delete_json_schemas(packages: list[str]) -> None:
    """delete all json schemas"""
    for pkg in packages:
        to_delete = output_directory / pkg
        if to_delete.exists():
            for file in to_delete.iterdir():
                file.unlink()


def get_models(pkg: str) -> Iterator[str]:
    """
    Get all models in a package
    """
    yield from (name for _, name, _ in pkgutil.iter_modules([str(root_directory / "src" / "bo4e" / pkg)]))


def get_classes(modl_name: str) -> list[tuple[str, type]]:
    """
    Get all classes in a module
    """
    modl = importlib.import_module(modl_name)
    return inspect.getmembers(modl, lambda member: inspect.isclass(member) and member.__module__ == modl_name)


def get_namespace(packages: list[str]) -> dict[str, tuple[str, str, PARSABLE_CLASS_TYPE]]:
    """
    Builds a dictionary with the classnames as keys and their module as tuples in the values. E.g.:
    {
        "Geschaeftsobjekt": ("bo", "geschaeftsobjekt"),
        "COM": ("com", "com"),
        ...
    }
    This function filters out all classes which names begin with an underscore.
    """
    namespace = {}
    for pkg in packages:
        for model in get_models(pkg):
            modl_name = f"bo4e.{pkg}.{model}"
            cls_list = get_classes(modl_name)
            for name, cls in cls_list:
                if not name.startswith("_") and name != "StrEnum":
                    namespace[name] = (pkg, model, cast(PARSABLE_CLASS_TYPE, cls))
    return namespace


def get_schema_json_dict(cls: Any) -> dict[str, Any]:
    """
    Get the json schema for a class
    """
    if issubclass(cls, BaseModel):
        schema_json_dict = cls.model_json_schema(schema_generator=GenerateJsonSchema)
    elif issubclass(cls, Enum):
        schema_json_dict = TypeAdapter(cls).json_schema(schema_generator=GenerateJsonSchema)
    else:
        raise ValueError(f"Class {cls} is neither a pydantic BaseModel nor an enum.")
    if "$defs" in schema_json_dict:
        del schema_json_dict["$defs"]
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


def generate_schema(file_path: Path, schema_json_dict: dict[str, Any]) -> None:
    """
    Generate the schema for a class
    """
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
    with open(file_path, "w+", encoding="utf-8") as json_schema_file:
        json_schema_file.write(json.dumps(schema_json_dict, indent=4, sort_keys=True, ensure_ascii=False))
        json_schema_file.write("\n")


def replace_refs(
    schema_json_dict: dict[str, Any], namespace: dict[str, tuple[str, str, PARSABLE_CLASS_TYPE]], target_version: str
) -> None:
    """
    Replace the definition of a class with an online reference to the definition
    """

    def traverse_list(obj: list[Any]) -> None:
        for item in obj:
            if isinstance(item, dict):
                traverse_dict(item)
            elif isinstance(item, list):
                traverse_list(item)

    def traverse_dict(obj: dict[str, Any]) -> None:
        for key, value in obj.items():
            if isinstance(value, dict):
                traverse_dict(value)
            elif isinstance(value, list):
                traverse_list(value)
            elif key == "$ref":
                match = OLD_REF_TEMPLATE.match(value)
                if match is None:
                    raise ValueError(f"Invalid reference: {value}")
                ref_model = match.group("model")
                if ref_model not in namespace:
                    raise ValueError(f"Unknown referenced model {ref_model}")
                if namespace[ref_model][0] == "":
                    obj["$ref"] = NEW_REF_TEMPLATE_ROOT.format(model=ref_model, version=target_version)
                else:
                    obj["$ref"] = NEW_REF_TEMPLATE.format(
                        pkg=namespace[ref_model][0], model=ref_model, version=target_version
                    )

    traverse_dict(schema_json_dict)


@click.command()
@click.option(
    "--mode",
    "-m",
    help="use 'validate' to validate existing schemas or 'generate' to generate new schemas",
    required=True,
    type=click.Choice(["validate", "generate"]),
)
@click.option(
    "--target-version",
    "-t",
    help="the tagged version known inside the release workflow",
    required=False,
    type=click.STRING,
    envvar="TARGET_VERSION",
    default="v0.0.0",
)
def generate_or_validate_json_schemas(mode: Literal["validate", "generate"], target_version: str) -> None:
    """generate json schemas for all BOs and COMs"""
    packages = ["bo", "com", "enum"]

    if mode == "generate":
        delete_json_schemas(packages)

    namespace = get_namespace(packages)
    namespace[ZusatzAttribut.__name__] = ("", "zusatzattribut", ZusatzAttribut)

    for name, (pkg, _, cls) in namespace.items():
        _logger.debug("Processing %s", name)

        if pkg == "":
            file_path = output_directory / (name + ".json")
        else:
            file_path = output_directory / pkg / (name + ".json")

        schema_json_dict = get_schema_json_dict(cls)
        replace_refs(schema_json_dict, namespace, target_version)

        if mode == "validate":
            validate_schema(file_path, schema_json_dict, name)
        elif mode == "generate":
            generate_schema(file_path, schema_json_dict)
            _logger.info("Generated schema for %s", name)
        else:
            raise ValueError(f"Unknown mode '{mode}'")


if __name__ == "__main__":
    generate_or_validate_json_schemas()  # pylint:disable=no-value-for-parameter
