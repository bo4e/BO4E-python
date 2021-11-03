# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Sparte(StrEnum):
    """
    Unterscheidungsmöglichkeiten für die Sparte.
    """

    STROM = "STROM"
    GAS = "GAS"
    FERNWAERME = "FERNWAERME"
    NAHWAERME = "NAHWAERME"
    WASSER = "WASSER"
    ABWASSER = "ABWASSER"
