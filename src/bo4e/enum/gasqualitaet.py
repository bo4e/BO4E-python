from enum import Enum


class Gasqualitaet(str, Enum):
    """
    Unterscheidung für hoch- und niedrig-kalorisches Gas.
    """

    H_GAS = "H_GAS"  # High Caloric Gas
    L_GAS = "L_GAS"  # Low Caloric Gas
