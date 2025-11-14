# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Preisreferenz(StrEnum):
    """
    Referenz worauf sich eine Preisposition bezieht.
    """

    ENERGIEMENGE = "ENERGIEMENGE"
    LEISTUNG = "LEISTUNG"
    ZEITRAUM = "ZEITRAUM"
    ANZAHL = "ANZAHL"
    PAUSCHAL = "PAUSCHAL"
