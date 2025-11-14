# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Wiederholungstyp(StrEnum):
    """
    Gibt an zu welchen Tagen etwas wiederholt werden soll.
    """

    TAEGLICH = "TAEGLICH"
    WERKTAGS = "WERKTAGS"
    WOCHENENDE = "WOCHENENDE"
    FEIERTAGS = "FEIERTAGS"

    MONTAGS = "MONTAGS"
    DIENSTAGS = "DIENSTAGS"
    MITTWOCHS = "MITTWOCHS"
    DONNERTAGS = "DONNERTAGS"
    FREITAGS = "FREITAGS"
    SAMSTAGS = "SAMSTAGS"
    SONNTAGS = "SONNTAGS"
