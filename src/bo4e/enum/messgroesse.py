# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messgroesse(StrEnum):
    """
    Gibt die physikalische Größe an, die gemessen wurde.
    """

    STROM = "STROM"  #: STROM
    SPANNUNG = "SPANNUNG"  #: SPANNUNG
    WIRKLEISTUNG = "WIRKLEISTUNG"  #: WIRKLEISTUNG
    BLINDLEISTUNG = "BLINDLEISTUNG"  #: BLINDLEISTUNG
    DRUCK = "DRUCK"  #: DRUCK
    LASTGANG = "LASTGANG"  #: LASTGANG
    LASTPROFIL = "LASTPROFIL"  #: LASTPROFIL
    TEMPERATUR = "TEMPERATUR"  #: TEMPERATUR
    ZZAHL = "ZZAHL"  #: Zustandszahl
    BRENNWERT = "BRENNWERT"  #: BRENNWERT
    GRADTZAGSZAHLEN = "GRADTZAGSZAHLEN"  #: GRADTZAGSZAHLEN
    VOLUMENSTROM = "VOLUMENSTROM"  #: VOLUMENSTROM
    PREISE = "PREISE"  #: PREISE
