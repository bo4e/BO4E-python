# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Zeiteinheit(StrEnum):
    """
    Auflistung möglicher Einheiten zur Verwendung in zeitbezogenen Angaben.
    """

    SEKUNDE = "SEKUNDE"  #: Sekunde
    MINUTE = "MINUTE"  #: Minute
    STUNDE = "STUNDE"  #: Stunde
    VIERTEL_STUNDE = "VIERTEL_STUNDE"  #: Viertelstunde
    TAG = "TAG"  #: Tag
    WOCHE = "WOCHE"  #: Woche
    MONAT = "MONAT"  #: Monat
    QUARTAL = "QUARTAL"  #: Quartal
    HALBJAHR = "HALBJAHR"  #: Halbjahr
    JAHR = "JAHR"  #: Jahr
