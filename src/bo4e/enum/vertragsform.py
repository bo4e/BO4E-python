# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Vertragsform(StrEnum):
    """
    Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen.
    """

    ONLINE = "ONLINE"  #: Online
    DIREKT = "DIREKT"  #: Direkt
    FAX = "FAX"  #: Auftragsfax
