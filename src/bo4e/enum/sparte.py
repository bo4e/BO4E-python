from enum import Enum


class Sparte(str, Enum):
    """
    Unterscheidungsmöglichkeiten für die Sparte.
    """

    STROM = "STROM"
    GAS = "GAS"
    FERNWAERME = "FERNWAERME"
    NAHWAERME = "NAHWAERME"
    WASSER = "WASSER"
    ABWASSER = "ABWASSER"
