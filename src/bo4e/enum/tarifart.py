# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Tarifart(StrEnum):
    """
    Die Tarifart wird verwendet zur Charakterisierung von Zählern und daraus resultierenden Tarifen.
    """

    EINTARIF = "EINTARIF"  #: Eintarif
    ZWEITARIF = "ZWEITARIF"  #: Zweitarif
    MEHRTARIF = "MEHRTARIF"  #: Mehrtarif
    SMART_METER = "SMART_METER"  #: Smart Meter Tarif
    LEISTUNGSGEMESSEN = "LEISTUNGSGEMESSEN"  #: Leistungsgemessener Tarif
