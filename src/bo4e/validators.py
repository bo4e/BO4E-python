"""
Contains validators for BO s and COM s classes.
"""
from datetime import datetime
from typing import Protocol

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


# pylint:disable=too-few-public-methods
class _VonBisType(Protocol):
    """
    a protocol for all classes that have an inclusive start and exclusive end
    """

    def get_inclusive_start(self) -> datetime:
        """
        should return the inclusive start of the timeslice
        """
        pass

    def get_exclusive_end(self) -> datetime:
        """
        should return the exclusive end of the timeslice
        """
        pass


def check_bis_is_later_than_von(instance: _VonBisType, attribute, value):
    """
    assert that 'bis' is later than 'von'
    """
    start = instance.get_inclusive_start()
    end = instance.get_exclusive_end()
    if not end >= start:
        raise ValueError(f"The end '{end}' has to be later than the start '{start}'")
