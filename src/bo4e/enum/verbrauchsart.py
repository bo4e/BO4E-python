# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Verbrauchsart(StrEnum):
    """
    Verbrauchsart einer Marktlokation.
    """

    KL = "KL"  #: Kraft/Licht
    KLW = "KLW"  #: Kraft/Licht/Wärme
    KLWS = "KLWS"  #: Kraft/Licht/Wärme/Speicherheizung
    W = "W"  #: Wärme
    WS = "WS"  #: Wärme/Speicherheizung
