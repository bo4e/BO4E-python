# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Lokationstyp(StrEnum):
    """
    Gibt an, ob es sich um eine Markt- oder Messlokation handelt.
    """

    MALO = "MALO"  #: Marktlokation
    MELO = "MELO"  #: Messlokation
