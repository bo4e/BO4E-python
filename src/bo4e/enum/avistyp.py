"""Contains Enums for Avisposition"""
from bo4e.enum.strenum import StrEnum


class AvisTyp(StrEnum):
    """Gibt den Typ des Avis an. (REMADV BGM 1001)."""

    ABGELEHNTE_FORDERUNG = "ABGELEHNTE_FORDERUNG"  #: Abgelehnte Forderung
    ZAHLUNGSAVIS = "ZAHLUNGSAVIS"  #: Zahlungsavis
