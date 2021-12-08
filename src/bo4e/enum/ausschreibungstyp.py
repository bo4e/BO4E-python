# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Ausschreibungstyp(StrEnum):
    """
    Aufzählung für die Typisierung von Ausschreibungen.
    """

    PRIVATRECHTLICH = "PRIVATRECHTLICH"  #: privat-rechtlich
    OEFFENTLICHRECHTLICH = "OEFFENTLICHRECHTLICH"  #: öffentlich-rechtlich
    EUROPAWEIT = "EUROPAWEIT"  #: europaweit
