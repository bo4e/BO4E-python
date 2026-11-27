# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tarifzeit(StrEnum):
    """
    Zur Kennzeichnung verschiedener Tarifzeiten, beispielsweise zur Bepreisung oder zur Verbrauchsermittlung.
    """

    HT = "HT"
    """Tarifzeit für Hochtarif bei Mehrtarif-Konfigurationen"""
    NT = "NT"
    """Tarifzeit für Niedrigtarif bei Mehrtarif-Konfigurationen"""
    ST = "ST"
    """Tarifzeit für Standardtarif bei Mehrtarif-Konfigurationen"""
