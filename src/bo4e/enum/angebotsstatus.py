# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Angebotsstatus(StrEnum):
    """
    Gibt den Status eines Angebotes an.
    """

    KONZEPTION  #: Konzeption
    UNVERBINDLICH  #: unverbindlich
    VERBINDLICH  #: verbindlich
    BEAUFTRAGT  #: beauftragt
    UNGUELTIG  #: ungültig
    ABGELEHNT  #: abgelehnt
    NACHGEFASST  #: nachgefasst
    AUSSTEHEND  #: ausstehend
    ERLEDIGT  #: erledigt
