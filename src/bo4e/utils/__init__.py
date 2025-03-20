"""
utils necessary for reflection/inspection and documentation runs
"""

from typing import TypeVar

from pydantic import BaseModel

from ..version import __gh_version__

T = TypeVar("T", bound=BaseModel)


def postprocess_docstring(cls: type[T]) -> type[T]:
    """
    Postprocess the docstring to inject the __gh_version__ for proper linking of the JSON-schemas.
    Note that doc-strings in Python have to be string literals, so we cannot use f-strings.
    Additionally, we add the comments to the description of the fields to enable the generation of JSON-Schemas with
    proper descriptions.
    """
    if cls.__doc__ is not None:
        cls.__doc__ = cls.__doc__.format(__gh_version__=__gh_version__)
    return cls
