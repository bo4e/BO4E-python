# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messgroesse(StrEnum):
    """
    Gibt die physikalische Größe an, die gemessen wurde.
    """

    STROM  #: STROM
    SPANNUNG  #: SPANNUNG
    WIRKLEISTUNG  #: WIRKLEISTUNG
    BLINDLEISTUNG  #: BLINDLEISTUNG
    DRUCK  #: DRUCK
    LASTGANG  #: LASTGANG
    LASTPROFIL  #: LASTPROFIL
    TEMPERATUR  #: TEMPERATUR
    ZZAHL  #: ZZAHL
    BRENNWERT  #: BRENNWERT
    GRADTZAGSZAHLEN  #: GRADTZAGSZAHLEN
    VOLUMENSTROM  #: VOLUMENSTROM
    PREISE  #: PREISE
