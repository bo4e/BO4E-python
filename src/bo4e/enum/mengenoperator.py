# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Mengenoperator(StrEnum):
    """
    Angabe, wie eine Menge in Bezug auf einen Wert zu bilden ist.
    """

    KLEINER_ALS  #: Alle Objekte mit einem Wert kleiner als der Bezugswert
    GROESSER_ALS  #: Alle Objekte mit einem Wert größer als der Bezugswert
    GLEICH  #: Alle Objekte mit gleichem Wert
