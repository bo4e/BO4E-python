"""
This module contains the logic to create the compatibility matrix from a list of changes.
"""

import csv
import itertools
from enum import StrEnum
from pathlib import Path
from typing import Any as _Any
from typing import Mapping, Sequence

from . import change_schemas


class ChangeSymbol(StrEnum):
    """
    This enum class lists the different symbols of changes in the compatibility matrix.
    """

    CHANGE_NONE = "🟢"
    CHANGE_NON_CRITICAL = "🟡"
    CHANGE_CRITICAL = "🔴"
    NON_EXISTENT = "\\-"
    ADDED = "➕"
    REMOVED = "➖"


def determine_symbol(
    changes: Sequence[change_schemas.Change], namespace: Sequence[tuple[str, ...]], cls: tuple[str, ...]
) -> ChangeSymbol:
    """
    Determine the symbol of a change.
    """
    if len(changes) == 1 and changes[0].type == change_schemas.ChangeType.CLASS_REMOVED:
        return ChangeSymbol.REMOVED
    if len(changes) == 1 and changes[0].type == change_schemas.ChangeType.CLASS_ADDED:
        return ChangeSymbol.ADDED
    if cls not in namespace:
        return ChangeSymbol.NON_EXISTENT
    if len(changes) == 0:
        return ChangeSymbol.CHANGE_NONE

    assert all(
        change.type not in (change_schemas.ChangeType.CLASS_ADDED, change_schemas.ChangeType.CLASS_REMOVED)
        for change in changes
    ), "Internal error: CLASS_ADDED and CLASS_REMOVED must be the only change per class if present."
    if any(change_schemas.is_change_critical(change) for change in changes):
        return ChangeSymbol.CHANGE_CRITICAL
    return ChangeSymbol.CHANGE_NON_CRITICAL


def create_compatibility_matrix_csv(
    output: Path,
    versions: Sequence[str],
    namespaces: Mapping[str, Sequence[tuple[str, ...]]],
    changes: Mapping[tuple[str, str], Sequence[change_schemas.Change]],
) -> None:
    """
    Create a compatibility matrix csv file from the given changes.
    """
    with open(output, "w", encoding="utf-8") as file:
        csv_writer = csv.writer(file, delimiter=",", lineterminator="\n", escapechar="/")
        csv_writer.writerow(("", *versions[1:]))
        all_classes: set[tuple[str, ...]] = set(itertools.chain.from_iterable(namespaces.values()))

        for class_path in sorted(all_classes, key=lambda cls: tuple(cls_part.lower() for cls_part in cls)):
            row = [class_path[-1]]
            class_path_str = "/".join(class_path) + "#"
            for version_old, version_new in itertools.pairwise(versions):
                changes_related_to_class = [
                    change
                    for change in changes[(version_old, version_new)]
                    if change.old_trace.startswith(class_path_str) or change.new_trace.startswith(class_path_str)
                ]
                row.append(determine_symbol(changes_related_to_class, namespaces[version_new], class_path).value)
            csv_writer.writerow(row)
