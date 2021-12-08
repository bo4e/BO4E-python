# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Preisstatus(StrEnum):
    """
    Statusinformation für Preise
    """

    VORLAEUFIG = "VORLAEUFIG"  #: vorläufig
    ENDGUELTIG = "ENDGUELTIG"  #: endgültig
