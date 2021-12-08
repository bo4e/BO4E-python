# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messart(StrEnum):
    """
    Gibt an, auf welche Art gemessen wurde.
    """

    AKTUELLERWERT = "AKTUELLERWERT"  #: AKTUELLERWERT
    MITTELWERT = "MITTELWERT"  #: MITTELWERT
    MAXIMALWERT = "MAXIMALWERT"  #: MAXIMALWERT
