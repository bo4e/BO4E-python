# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Ausschreibungstyp(StrEnum):
    """
    Aufzählung für die Typisierung von Ausschreibungen.
    """

    PRIVATRECHTLICH  #: privat-rechtlich
    OEFFENTLICHRECHTLICH  #: öffentlich-rechtlich
    EUROPAWEIT  #: europaweit
