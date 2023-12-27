"""
utils necessary for reflection/inspection and documentation runs
"""
from typing import TypeVar

from pydantic import BaseModel
from pydantic._internal._fields import PydanticGeneralMetadata
from pydantic.fields import FieldInfo

from ..version import __gh_version__


def is_constrained_str(model_field: FieldInfo) -> bool:
    """
    returns True if the given model_field is a constrained string
    """
    for metad in model_field.metadata:
        if isinstance(metad, PydanticGeneralMetadata):
            if hasattr(metad, "pattern"):
                return True
    return False
    # return isinstance(model_field.outer_type_, type) and issubclass(model_field.outer_type_, str)


T = TypeVar("T", bound=BaseModel)


def postprocess_docstring(cls: type[T]) -> type[T]:
    """
    Postprocess the docstring to inject the __gh_version__ for proper linking of the JSON-schemas.
    Note that doc-strings in Python have to be string literals, so we cannot use f-strings.
    """
    if cls.__doc__ is not None:
        cls.__doc__ = cls.__doc__.format(__gh_version__=__gh_version__)
    return cls
