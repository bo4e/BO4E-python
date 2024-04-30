"""
Contains the classes to model changes between two BO4E versions.
"""

from enum import StrEnum
from typing import Any, Iterable

from pydantic import BaseModel


class ChangeType(StrEnum):
    """
    This enum class lists the different types of changes of a single change between two BO4E versions.
    """

    FIELD_ADDED = "field_added"
    FIELD_REMOVED = "field_removed"
    FIELD_DEFAULT_CHANGED = "field_default_changed"
    FIELD_DESCRIPTION_CHANGED = "field_description_changed"
    # field type change types
    FIELD_CARDINALITY_CHANGED = "field_cardinality_changed"
    FIELD_REFERENCE_CHANGED = "field_reference_changed"
    FIELD_STRING_FORMAT_CHANGED = "field_string_format_changed"
    FIELD_ANY_OF_TYPE_ADDED = "field_any_of_type_added"
    FIELD_ANY_OF_TYPE_REMOVED = "field_any_of_type_removed"
    FIELD_ALL_OF_TYPE_ADDED = "field_all_of_type_added"
    FIELD_ALL_OF_TYPE_REMOVED = "field_all_of_type_removed"
    FIELD_TYPE_CHANGED = "field_type_changed"  # An arbitrary unclassified change in type

    CLASS_ADDED = "class_added"
    CLASS_REMOVED = "class_removed"
    CLASS_DESCRIPTION_CHANGED = "class_description_changed"

    ENUM_VALUE_ADDED = "enum_value_added"
    ENUM_VALUE_REMOVED = "enum_value_removed"


class Change(BaseModel):
    """
    This pydantic class models a single change between two BO4E versions.
    """

    type: ChangeType
    old: Any
    new: Any
    old_trace: str
    new_trace: str

    def __str__(self) -> str:
        return f"{self.type}: {self.old} -> {self.new}"


def is_change_critical(change: Change) -> bool:
    """
    This function checks if a change is critical i.e. if the new value is incompatible to the old value.
    """
    return change.type in (
        ChangeType.FIELD_REMOVED,
        ChangeType.FIELD_TYPE_CHANGED,
        ChangeType.FIELD_CARDINALITY_CHANGED,
        ChangeType.FIELD_REFERENCE_CHANGED,
        ChangeType.FIELD_STRING_FORMAT_CHANGED,
        ChangeType.FIELD_ANY_OF_TYPE_ADDED,
        ChangeType.FIELD_ANY_OF_TYPE_REMOVED,
        ChangeType.FIELD_ALL_OF_TYPE_ADDED,
        ChangeType.FIELD_ALL_OF_TYPE_REMOVED,
        ChangeType.CLASS_REMOVED,
        ChangeType.ENUM_VALUE_REMOVED,
    )


def filter_non_crit(changes: Iterable[Change]) -> Iterable[Change]:
    """
    This function filters out all non-critical changes.
    """
    return (change for change in changes if is_change_critical(change))
