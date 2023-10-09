# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Befestigungsart(StrEnum):
    """
    Befestigungsart von Zählern
    """

    STECKTECHNIK = "STECKTECHNIK"  #: STECKTECHNIK
    DREIPUNKT = "DREIPUNKT"  #: DREIPUNKT
    HUTSCHIENE = "HUTSCHIENE"  #: HUTSCHIENE
    EINSTUTZEN = "EINSTUTZEN"  #: EINSTUTZEN
    ZWEISTUTZEN = "ZWEISTUTZEN"  #: ZWEISTUTZEN
