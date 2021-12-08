# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tarifzeit(StrEnum):
    """
    Zur Kennzeichnung verschiedener Tarifzeiten, beispielsweise zur Bepreisung oder zur Verbrauchsermittlung.
    """

    TZ_STANDARD = "TZ_STANDARD"  #: Tarifzeit Standard für Eintarif-Konfigurationen
    TZ_HT = "TZ_HT"  #: Tarifzeit für Hochtarif bei Mehrtarif-Konfigurationen
    TZ_NT = "TZ_NT"  #: Tarifzeit für Niedrigtarif bei Mehrtarif-Konfigurationen
