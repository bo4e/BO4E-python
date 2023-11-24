# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Mengeneinheit(StrEnum):
    """
    Einheit: Messgrößen, die per Messung oder Vorgabe ermittelt werden können.
    """

    W = "W"  #: Watt
    WH = "WH"  #: Wattstunde
    KW = "KW"  #: Kilowatt
    KWH = "KWH"  #: Kilowattstunde
    KVARH = "KVARH"  #: Kilovarstunde
    MW = "MW"  #: Megawatt
    MWH = "MWH"  #: Megawattstunde
    STUECK = "STUECK"  #: Stückzahl
    KUBIKMETER = "KUBIKMETER"  #: Kubikmeter (Gas)
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
    PROZENT = "PROZENT"  #: Prozent
    KVAR = "KVAR"  #: Kilovar
