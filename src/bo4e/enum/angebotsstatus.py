# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Angebotsstatus(StrEnum):
    """
    Gibt den Status eines Angebotes an.
    """

    KONZEPTION = "KONZEPTION"  #: Konzeption
    UNVERBINDLICH = "UNVERBINDLICH"  #: unverbindlich
    VERBINDLICH = "VERBINDLICH"  #: verbindlich
    BEAUFTRAGT = "BEAUFTRAGT"  #: beauftragt
    UNGUELTIG = "UNGUELTIG"  #: ungültig
    ABGELEHNT = "ABGELEHNT"  #: abgelehnt
    NACHGEFASST = "NACHGEFASST"  #: nachgefasst
    AUSSTEHEND = "AUSSTEHEND"  #: ausstehend
    ERLEDIGT = "ERLEDIGT"  #: erledigt
