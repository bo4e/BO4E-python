# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Steuerart(StrEnum):
    """
    Zur Kennzeichnung verschiedener Steuerarten.
    """

    RCV = "RCV"
    """Reverse Charge Verfahren (Umkehrung der Steuerpflicht)"""
    UST = "UST"
    """Umsatzsteuer"""
    VST = "VST"
    """Vorsteuer"""
