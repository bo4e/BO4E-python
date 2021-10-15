"""
Unterscheidungsmöglichkeiten für die Sparte.
"""
from enum import Enum

Sparte = Enum(
    "Sparte",
    {
        "STROM": "STROM",
        "GAS": "GAS",
        "FERNWAERME": "FERNWAERME",
        "NAHWAERME": "NAHWAERME",
        "WASSER": "WASSER",
        "ABWASSER": "ABWASSER",
    },
)
