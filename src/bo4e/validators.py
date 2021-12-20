"""
Contains validators for BO s and COM s classes.
"""

from bo4e.enum.aufabschlagstyp import AufAbschlagstyp

# pylint: disable=unused-argument


def check_list_length_at_least_one(instance, attribute, value):
    """
    Check that minimal list length is at least one.
    """
    if len(value) < 1:
        raise ValueError(f"List {attribute.name} must not be empty.")


def einheit_only_for_abschlagstyp_absolut(instance, attribute, value):
    """
    Check that einheit is only there if abschlagstyp is absolut.
    Currently (2021-12-15) only used in COM AufAbschlag.
    """
    if value and (not instance.auf_abschlagstyp or (instance.auf_abschlagstyp != AufAbschlagstyp.ABSOLUT)):
        raise ValueError("Only state einheit if auf_abschlagstyp is absolute.")
