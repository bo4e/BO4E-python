"""
Utility functions for tests.
"""
from pathlib import Path

from pydantic import BaseModel


def parse_file(model: type[BaseModel], path_to_file: Path | str) -> BaseModel:
    """
    Parses the given file as JSON and validates it against the given model.
    If the file is not valid JSON or does not match the model, a ValidationError is raised.
    Returns a validated instance of the given model.
    """
    with open(path_to_file, encoding="utf-8") as file:
        content = file.read()
    return model.model_validate_json(content)
