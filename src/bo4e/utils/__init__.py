"""
utils necessary for reflection/inspection and documentation runs
"""

from pydantic._internal._fields import PydanticGeneralMetadata
from pydantic.fields import FieldInfo


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
