"""
Contains validators for BO s and COM s classes.
"""
import re
from datetime import datetime
from typing import Optional, Protocol

from pydantic_core.core_schema import ValidationInfo

from bo4e.enum.aufabschlagstyp import AufAbschlagstyp

# pylint: disable=unused-argument
from bo4e.enum.waehrungseinheit import Waehrungseinheit


def einheit_only_for_abschlagstyp_absolut(cls, value: Waehrungseinheit, validation_info: ValidationInfo) -> Waehrungseinheit:  # type: ignore[no-untyped-def]
    """
    Check that einheit is only there if abschlagstyp is absolut.
    Currently, (2021-12-15) only used in COM AufAbschlag.
    """
    values = validation_info.data  # type:ignore[attr-defined]
    if value and (not values["auf_abschlagstyp"] or (values["auf_abschlagstyp"] != AufAbschlagstyp.ABSOLUT)):
        raise ValueError("Only state einheit if auf_abschlagstyp is absolute.")
    return value


# pylint:disable=too-few-public-methods
class _VonBisType(Protocol):
    """
    a protocol for all classes that have an inclusive start and exclusive end
    """

    @staticmethod
    def _get_inclusive_start(values: ValidationInfo) -> Optional[datetime]:
        """
        should return the inclusive start of the timeslice
        """

    # def _get_exclusive_end(self) -> Optional[datetime]:
    #     """
    #     should return the exclusive end of the timeslice
    #     """


def check_bis_is_later_than_von(cls, value: datetime, values: ValidationInfo):  # type: ignore[no-untyped-def]
    """
    assert that 'bis' is later than 'von'
    """
    # we want access to private methods here because these helper methods should be "hidden"
    start = cls._get_inclusive_start(values)  # pylint: disable=protected-access
    end = value
    if start and end and not end >= start:
        raise ValueError(f"The end '{end}' has to be later than the start '{start}'")
    return value


# pylint:disable=line-too-long
#: a regular expression that should match all OBIS Kennziffern
OBIS_PATTERN = r"((1)-((?:[0-5]?[0-9])|(?:6[0-5])):((?:[1-8]|99))\.((?:6|8|9|29))\.([0-9]{1,2})|(7)-((?:[0-5]?[0-9])|(?:6[0-5])):(.{1,2})\.(.{1,2})\.([0-9]{1,2}))"
# TODO: Maybe create custom data type for OBIS. See https://pydantic-docs.helpmanual.io/usage/types/#custom-data-types

_malo_id_pattern = re.compile(r"^[1-9]\d{10}$")


# pylint: disable=unused-argument
def validate_marktlokations_id(cls, marktlokations_id: str, values: ValidationInfo) -> str:  # type: ignore[no-untyped-def]
    """
    A validator for marktlokations IDs
    """
    if not marktlokations_id:
        raise ValueError("The marktlokations_id must not be empty.")
    if not _malo_id_pattern.match(marktlokations_id):
        raise ValueError(f"The Marktlokations-ID '{marktlokations_id}' does not match {_malo_id_pattern.pattern}")
    expected_checksum = _get_malo_id_checksum(marktlokations_id)
    actual_checksum = marktlokations_id[10:11]
    if expected_checksum != actual_checksum:
        # pylint: disable=line-too-long
        raise ValueError(
            f"The Marktlokations-ID '{marktlokations_id}' has checksum '{actual_checksum}' but '{expected_checksum}' was expected."
        )
    return marktlokations_id


def _get_malo_id_checksum(malo_id: str) -> str:
    """
    Get the checksum of a marktlokations id.
    a) Quersumme aller Ziffern in ungerader Position
    b) Quersumme aller Ziffern auf gerader Position multipliziert mit 2
    c) Summe von a) und b) d) Differenz von c) zum nächsten Vielfachen von 10 (ergibt sich hier 10, wird die
       Prüfziffer 0 genommen
    https://bdew-codes.de/Content/Files/MaLo/2017-04-28-BDEW-Anwendungshilfe-MaLo-ID_Version1.0_FINAL.PDF
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
