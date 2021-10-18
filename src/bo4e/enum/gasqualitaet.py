"""
Unterscheidung für hoch- und niedrig-kalorisches Gas.
"""
from enum import Enum

Gasqualitaet = Enum(
    "Gasqualitaet",
    {
        "H_GAS": "H_GAS",  # High Caloric Gas
        "L_GAS": "L_GAS",  # Low Caloric Gas
    },
)  # type: ignore
