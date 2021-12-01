# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tarifregionskriterium(StrEnum):
    """
    Mit diesen Kriterien können regionale Bereiche definiert werden.
    """

    NETZ_NUMMER  #: Netznummer
    POSTLEITZAHL  #: Postleitzahl
    ORT  #: Ort
    GRUNDVERSORGER_NUMMER  #: Nummer des Grundversorgers
    REGION  #: Referenz auf ein BO Region (URL)
