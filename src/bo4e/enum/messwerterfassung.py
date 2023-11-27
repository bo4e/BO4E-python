# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messwerterfassung(StrEnum):
    """
    Die Messwerterfassung des Zählers
    """

    FERNAUSLESBAR = "FERNAUSLESBAR"  #: fernauslesbare Zähler
    MANUELL_AUSGELESENE = "MANUELL_AUSGELESENE"  #: manuell ausgelesene Zähler
