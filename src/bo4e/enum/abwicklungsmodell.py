# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Abwicklungsmodell(StrEnum):
    """
    Art des Abwicklungsmodell (E-Mob)
    """

    MODELL_1 = "MODELL_1"  #: Modell 1 "Bilanzierung an der Marktlokation"
    MODELL_2 = "MODELL_2"  #: Modell 2 "Bilanzierung im Bilanzierungsgebiet (BG) des LPB
