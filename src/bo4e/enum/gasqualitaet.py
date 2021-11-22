# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Gasqualitaet(StrEnum):
    """
    Unterscheidung für hoch- und niedrig-kalorisches Gas.
    """

    H_GAS = "H_GAS"  #: High Caloric Gas
    L_GAS = "L_GAS"  #: Low Caloric Gas
