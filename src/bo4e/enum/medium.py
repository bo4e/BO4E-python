# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Medium(StrEnum):
    """
    Gibt ein physikalisches Medium an.
    """

    STROM = "STROM"  #: STROM
    GAS = "GAS"  #: GAS
    WASSER = "WASSER"  #: WASSER
    DAMPF = "DAMPF"  #: DAMPF
