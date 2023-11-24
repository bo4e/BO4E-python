# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Registeranzahl(StrEnum):
    """
    Die Registeranzahl wird verwendet zur Charakterisierung von Zählern und daraus resultierenden Tarifen.
    """

    EINTARIF = "EINTARIF"  #: Eintarif
    ZWEITARIF = "ZWEITARIF"  #: Zweitarif
    MEHRTARIF = "MEHRTARIF"  #: Mehrtarif
