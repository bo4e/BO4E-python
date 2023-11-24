# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Waermenutzung(StrEnum):
    """
    Wärmenutzung Marktlokation
    """

    SPEICHERHEIZUNG = "SPEICHERHEIZUNG"  #: Speicherheizung
    WAERMEPUMPE = "WAERMEPUMPE"  #: Wärmepumpe
    DIREKTHEIZUNG = "DIREKTHEIZUNG"  #: Direktheizung
