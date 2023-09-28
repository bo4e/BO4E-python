"""
This script is run in the tox 'json_schemas' environment.
"""

import importlib
import inspect
import json
import logging
import pathlib
import pkgutil
from typing import Literal

import click

_logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--mode",
    "-m",
    help="use 'validate' to validate existing schemas or 'generate' to generate new schemas",
    required=True,
    type=click.Choice(["validate", "generate"]),
)
def generate_json_schemas(mode: Literal["validate", "generate"]) -> None:
    """generate json schemas for all BOs and COMs"""
    for pkg in ["bo", "com"]:
        modls = [
            name
            for _, name, _ in pkgutil.iter_modules([str(pathlib.Path(__file__).parent.parent / "src" / "bo4e" / pkg)])
        ]
        for model in modls:
            modl_name = f"bo4e.{pkg}.{model}"
            modl = importlib.import_module(modl_name)
            # pylint: disable=cell-var-from-loop
            cls_list = inspect.getmembers(
                modl, lambda member: inspect.isclass(member) and member.__module__ == modl_name
            )
            this_directory = pathlib.Path(__file__).parent.absolute()
            for name, cls in cls_list:
                _logger.info("Processing %s", name)
                file_path = this_directory / pkg / (name + ".json")  # pylint:disable=invalid-name
                schema_json_dict = cls.model_json_schema()
                if "definitions" in schema_json_dict:
                    for definition in schema_json_dict["definitions"].values():
                        # this sanitizing step is necessary since python 3.11
                        definition["description"] = definition["description"].strip()
                if mode == "validate":
                    with open(file_path, "r", encoding="utf-8") as json_schema_file:
                        existing_schema = json.load(json_schema_file)
                    if schema_json_dict != existing_schema:
                        raise ValueError(f"Schema for {name} has changed. Please run this script with mode 'generate'.")
                        # or call tox -e generate_json_schemas
                    _logger.debug("Schema for %s is consistent", name)
                elif mode == "generate":
                    with open(file_path, "w+", encoding="utf-8") as json_schema_file:
                        json_schema_file.write(
                            json.dumps(schema_json_dict, indent=4, sort_keys=True, ensure_ascii=False)
                        )
                        json_schema_file.write("\n")  # empty line at EOF for those with broken pre-commit hook ;)
                    _logger.debug("Generated schema for %s", name)
                else:
                    raise ValueError(f"Unknown mode '{mode}'")


if __name__ == "__main__":
    generate_json_schemas()  # pylint:disable=no-value-for-parameter
