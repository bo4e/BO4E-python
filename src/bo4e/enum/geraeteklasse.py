# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


# pylint: disable=line-too-long
class Geraeteklasse(StrEnum):
    """
    Auflistung möglicher übergreifenden Geräteklassen.
    """

    WANDLER = "WANDLER"  #: Wandler
    KOMMUNIKATIONSEINRICHTUNG = "KOMMUNIKATIONSEINRICHTUNG"  #: Kommunikationseinrichtung
    TECHNISCHE_STEUEREINRICHTUNG = "TECHNISCHE_STEUEREINRICHTUNG"  #: Technische Steuereinrichtung
    MENGENUMWERTER = "MENGENUMWERTER"  #: Mengenumwerter
    SMARTMETER_GATEWAY = "SMARTMETER_GATEWAY"  #: Smartmeter-Gateway
    STEUERBOX = "STEUERBOX"  #: Steuerbox
    ZAEHLEINRICHTUNG = "ZAEHLEINRICHTUNG"  #: Zaehleinrichtung
