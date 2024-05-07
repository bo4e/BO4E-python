"""
utils necessary for reflection/inspection and documentation runs
"""

import inspect
import re
from typing import TypeVar

from pydantic import BaseModel

from ..version import __gh_version__

T = TypeVar("T", bound=BaseModel)
REGEX_CLASS_START = re.compile(r"class \w+\(.*\):\s+\"{3}(?:(?:\"{0,2}[^\"])*)\"{3}\n")
# https://regex101.com/r/dQPi06/1


def add_comments_to_description(cls: type[T]) -> type[T]:
    """
    Add comments of fields to the description of the fields. This enables the generation of JSON-Schemas with proper
    descriptions.
    """
    code = inspect.getsource(cls)
    split_result = REGEX_CLASS_START.split(code)
    assert len(split_result) == 2, "The class source code structure is not as expected."
    fields_code = split_result[1]
    regex_comment_above = r"#: ?(?P<comment>[^\n]*)\n\s+{field_name}:"
    # https://regex101.com/r/aJrvol/1
    regex_comment_inline = r"{field_name}:[^:]*#: ?(?P<comment>[^\n]*)\n"
    # https://regex101.com/r/0PaUmw/1
    regex_comment_below = r"{field_name}:[^:]*\n(?P<indent> +)\"{3}(?P<comment>(?:\"{0,2}[^\"])*)\"{3}"
    # https://regex101.com/r/9HhOlD/1

    for field_name, field_info in cls.model_fields.items():
        if field_info.description is not None:
            continue
        # search for (single line) comments above the field
        match = re.search(regex_comment_above.format(field_name=field_name), fields_code)
        if match is not None:
            field_info.description = match.group("comment").strip()
            continue
        # search for (single line) comments inline with the field
        match = re.search(regex_comment_inline.format(field_name=field_name), fields_code)
        if match is not None:
            field_info.description = match.group("comment").strip()
            continue
        # search for (multi line) comments below the field
        match = re.search(regex_comment_below.replace("{field_name}", field_name), fields_code)
        if match is not None:
            field_info.description = match.group("comment").strip().replace("\n" + match.group("indent"), "\n")
            continue
        # Try to find the comment in the bases
        description = None
        for base in cls.__bases__:
            if base == BaseModel:
                continue
            if not issubclass(base, BaseModel):
                continue
            if field_name in base.model_fields:
                if base.model_fields[field_name].description is None:
                    add_comments_to_description(base)
                description = base.model_fields[field_name].description
                break
        if description is not None:
            field_info.description = description
            continue

        print(f"Could not find a comment for field {field_name} in class {cls}")

    # cls.model_rebuild(force=True)
    # Unnecessary here since the models will be rebuilt in __init__.py.
    # Keeping this here as comment though.
    return cls


def postprocess_docstring(cls: type[T]) -> type[T]:
    """
    Postprocess the docstring to inject the __gh_version__ for proper linking of the JSON-schemas.
    Note that doc-strings in Python have to be string literals, so we cannot use f-strings.
    Additionally, we add the comments to the description of the fields to enable the generation of JSON-Schemas with
    proper descriptions.
    """
    if cls.__doc__ is not None:
        cls.__doc__ = cls.__doc__.format(__gh_version__=__gh_version__)
    add_comments_to_description(cls)
    return cls
