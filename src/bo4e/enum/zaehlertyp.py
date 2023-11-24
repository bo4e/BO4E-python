# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Zaehlertyp(StrEnum):
    """
    Bei diesem Enum handelt es sich um die Abbildung von Zählertypen der Sparten Strom und Gas.
    """

    DREHSTROMZAEHLER = "DREHSTROMZAEHLER"  #: Drehstromzähler
    BALGENGASZAEHLER = "BALGENGASZAEHLER"  #: Balgengaszähler
    DREHKOLBENZAEHLER = "DREHKOLBENZAEHLER"  #: Drehkolbengaszähler
    LEISTUNGSZAEHLER = "LEISTUNGSZAEHLER"  #: leistungsmessender Zähler
    MAXIMUMZAEHLER = "MAXIMUMZAEHLER"  #: Maximumzähler
    TURBINENRADGASZAEHLER = "TURBINENRADGASZAEHLER"  #: Turbinenradgaszähler
    ULTRASCHALLGASZAEHLER = "ULTRASCHALLGASZAEHLER"  #: Ultraschallgaszähler
    WECHSELSTROMZAEHLER = "WECHSELSTROMZAEHLER"  #: Wechselstromzähler
    MODERNE_MESSEINRICHTUNG = "MODERNE_MESSEINRICHTUNG"  #: Moderne Messeinrichtung
    INTELLIGENTES_MESSSYSTEM = "INTELLIGENTES_MESSSYSTEM"  #: Intelligentes Messsystem
    ELEKTRONISCHER_ZAEHLER = "ELEKTRONISCHER_ZAEHLER"  #: Elektronischer Zähler
    WIRBELGASZAEHLER = "WIRBELGASZAEHLER"  #: Wirbelgaszähler
