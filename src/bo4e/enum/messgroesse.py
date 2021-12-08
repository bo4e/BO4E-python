# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messgroesse(StrEnum):
    """
    Gibt die physikalische Größe an, die gemessen wurde.
    """

    STROM = "STROM"  #: Strom
    SPANNUNG = "SPANNUNG"  #: Spannung
    WIRKLEISTUNG = "WIRKLEISTUNG"  #: Wirkleistung
    BLINDLEISTUNG = "BLINDLEISTUNG"  #: Blindleistung
    DRUCK = "DRUCK"  #: Druck
    LASTGANG = "LASTGANG"  #: Lastgang
    LASTPROFIL = "LASTPROFIL"  #: Lastprofil
    TEMPERATUR = "TEMPERATUR"  #: Temperatur
    ZZAHL = "ZZAHL"  #: Zustandszahl
    BRENNWERT = "BRENNWERT"  #: Brennwert
    GRADTZAGSZAHLEN = "GRADTZAGSZAHLEN"  #: Gradtagszahlen
    VOLUMENSTROM = "VOLUMENSTROM"  #: Volumenstrom
    PREISE = "PREISE"  #: Preise
