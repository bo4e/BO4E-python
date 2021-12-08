# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tarifregionskriterium(StrEnum):
    """
    Mit diesen Kriterien können regionale Bereiche definiert werden.
    """

    NETZ_NUMMER = "NETZ_NUMMER"  #: Netznummer
    POSTLEITZAHL = "POSTLEITZAHL"  #: Postleitzahl
    ORT = "ORT"  #: Ort
    GRUNDVERSORGER_NUMMER = "GRUNDVERSORGER_NUMMER"  #: Nummer des Grundversorgers
    REGION = "REGION"  #: Referenz auf ein BO Region (URL)
