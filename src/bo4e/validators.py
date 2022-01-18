"""
Contains validators for BO s and COM s classes.
"""
import re
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

_malo_id_pattern = re.compile(r"^[1-9][\d]{10}$")


# pylint: disable=unused-argument, no-self-use
def validate_marktlokations_id(self, marktlokations_id_attribute, value):
    """
    A validator for marktlokations IDs
    """
    if not value:
        raise ValueError("The marktlokations_id must not be empty.")
    if not _malo_id_pattern.match(value):
        raise ValueError(f"The {marktlokations_id_attribute.name} '{value}' does not match {_malo_id_pattern.pattern}")
    expected_checksum = _get_malo_id_checksum(value)
    actual_checksum = value[10:11]
    if expected_checksum != actual_checksum:
        # pylint: disable=line-too-long
        raise ValueError(
            f"The {marktlokations_id_attribute.name} '{value}' has checksum '{actual_checksum}' but '{expected_checksum}' was expected."
        )


def _get_malo_id_checksum(malo_id: str) -> str:
    """
    Get the checksum of a marktlokations id.
    a) Quersumme aller Ziffern in ungerader Position
    b) Quersumme aller Ziffern auf gerader Position multipliziert mit 2
    c) Summe von a) und b) d) Differenz von c) zum nächsten Vielfachen von 10 (ergibt sich hier 10, wird die
       Prüfziffer 0 genommen
    https://bdew-codes.de/Content/Files/MaLo/2017-04-28-BDEW-Anwendungshilfe-MaLo-ID_Version1.0_FINAL.PDF
    :param self:
    :return: the checksum as string
    """
    odd_checksum: int = 0
    even_checksum: int = 0
    # start counting at 1 to be consistent with the above description
    # of "even" and "odd" but stop at tenth digit.
    for i in range(1, 11):
        digit = malo_id[i - 1 : i]
        if i % 2 - 1 == 0:
            odd_checksum += int(digit)
        else:
            even_checksum += 2 * int(digit)
    result: int = (10 - ((even_checksum + odd_checksum) % 10)) % 10
    return str(result)
