# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Rechnungslegung(StrEnum):
    """
    Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen.
    """

    MONATSRECHN  #: monatsscharfe Rechnung
    ABSCHL_MONATSRECHN  #: Abschlag mit Monatsrechnung
    ABSCHL_JAHRESRECHN  #: Abschlag mit Jahresrechnung
    MONATSRECHN_JAHRESRECHN  #: Monatsrechnung mit Jahresrechnung
    VORKASSE  #: Vorkasse
