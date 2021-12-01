# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Preisstatus(StrEnum):
    """
    Statusinformation für Preise
    """

    VORLAEUFIG  #: vorläufig
    ENDGUELTIG  #: endgültig
