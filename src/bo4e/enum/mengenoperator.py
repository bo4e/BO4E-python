# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Mengenoperator(StrEnum):
    """
    Angabe, wie eine Menge in Bezug auf einen Wert zu bilden ist.
    """

    KLEINER_ALS = "KLEINER_ALS"  #: KLEINER_ALS
    GROESSER_ALS = "GROESSER_ALS"  #: GROESSER_ALS
    GLEICH = "GLEICH"  #: GLEICH
