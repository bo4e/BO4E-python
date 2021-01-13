"""
Unterscheidung für hoch- und niedrig-kalorisches Gas.
"""
from enum import Enum

_gasqualitaet = {
    "H_GAS": "H_GAS",  # High Caloric Gas
    "L_GAS": "L_GAS",  # Low Caloric Gas
}
Gasqualitaet = Enum("Gasqualitaet", _gasqualitaet)
