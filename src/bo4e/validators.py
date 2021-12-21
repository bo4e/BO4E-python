"""
Contains validators for BO s and COM s classes.
"""
from datetime import datetime
from typing import Optional, Protocol

import attr.validators

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
    Currently, (2021-12-15) only used in COM AufAbschlag.
    """
    if value and (not instance.auf_abschlagstyp or (instance.auf_abschlagstyp != AufAbschlagstyp.ABSOLUT)):
        raise ValueError("Only state einheit if auf_abschlagstyp is absolute.")


# pylint: disable=unused-argument
def check_list_length_is_one_or_two(instance, attribute, value):
    """
    Check if list length is one or two.
    So far only used in StandorteigenschaftenGas.
    """
    if len(value) == 0:
        raise ValueError(f"{attribute.name} must not be empty.")
    if len(value) > 2:
        raise ValueError(f"Maximum number of {attribute.name} is 2.")


# pylint:disable=too-few-public-methods
class _VonBisType(Protocol):
    """
    a protocol for all classes that have an inclusive start and exclusive end
    """

    def _get_inclusive_start(self) -> Optional[datetime]:
        """
        should return the inclusive start of the timeslice
        """

    def _get_exclusive_end(self) -> Optional[datetime]:
        """
        should return the exclusive end of the timeslice
        """


def check_bis_is_later_than_von(instance: _VonBisType, attribute, value):
    """
    assert that 'bis' is later than 'von'
    """
    # we want access to private methods here because these helper methods should be "hidden"
    start = instance._get_inclusive_start()  # pylint: disable=protected-access
    end = instance._get_exclusive_end()  # pylint: disable=protected-access
    if start and end and not end >= start:
        raise ValueError(f"The end '{end}' has to be later than the start '{start}'")


# pylint:disable=line-too-long
#: a regular expression that should match all OBIS Kennziffern
OBIS_PATTERN = r"((1)-((?:[0-5]?[0-9])|(?:6[0-5])):((?:[1-8]|99))\.((?:6|8|9|29))\.([0-9]{1,2})|(7)-((?:[0-5]?[0-9])|(?:6[0-5])):(.{1,2})\.(.{1,2})\.([0-9]{1,2}))"
#: an attr validator
obis_validator = attr.validators.matches_re(OBIS_PATTERN)
