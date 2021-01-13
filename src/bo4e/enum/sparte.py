"""
Unterscheidungsmöglichkeiten für die Sparte.
"""
from enum import Enum

_sparte = {
    "STROM": "STROM",
    "GAS": "GAS",
    "FERNWAERME": "FERNWAERME",
    "NAHWAERME": "NAHWAERME",
    "WASSER": "WASSER",
    "ABWASSER": "ABWASSER"
}
Sparte = Enum("Sparte", _sparte)
