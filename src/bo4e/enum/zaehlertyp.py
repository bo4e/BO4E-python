# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Zaehlertyp(StrEnum):
    """
    Bei diesem Enum handelt es sich um die Abbildung von Zählertypen der Sparten Strom und Gas.
    """

    DREHSTROMZAEHLER = "DREHSTROMZAEHLER"  #: Drehstromzähler
    BALGENGASZAEHLER = "BALGENGASZAEHLER"  #: Balgengaszähler
    DREHKOLBENZAEHLER = "DREHKOLBENZAEHLER"  #: Drehkolbengaszähler
    SMARTMETER = "SMARTMETER"  #: Smart Meter Zähler
    LEISTUNGSZAEHLER = "LEISTUNGSZAEHLER"  #: leistungsmessender Zähler
    MAXIMUMZAEHLER = "MAXIMUMZAEHLER"  #: Maximumzähler
    TURBINENRADGASZAEHLER = "TURBINENRADGASZAEHLER"  #: Turbinenradgaszähler
    ULTRASCHALLGASZAEHLER = "ULTRASCHALLGASZAEHLER"  #: Ultraschallgaszähler
    WECHSELSTROMZAEHLER = "WECHSELSTROMZAEHLER"  #: Wechselstromzähler
