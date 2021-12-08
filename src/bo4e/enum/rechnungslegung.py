# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Rechnungslegung(StrEnum):
    """
    Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen.
    """

    MONATSRECHN = "MONATSRECHN"  #: monatsscharfe Rechnung
    ABSCHL_MONATSRECHN = "ABSCHL_MONATSRECHN"  #: Abschlag mit Monatsrechnung
    ABSCHL_JAHRESRECHN = "ABSCHL_JAHRESRECHN"  #: Abschlag mit Jahresrechnung
    MONATSRECHN_JAHRESRECHN = "MONATSRECHN_JAHRESRECHN"  #: Monatsrechnung mit Jahresrechnung
    VORKASSE = "VORKASSE"  #: Vorkasse
