"""Contains enum class Avisposition"""
from bo4e.enum.strenum import StrEnum


class AvisTyp(StrEnum):
    """Gibt den Typ des Avis an. (REMADV BGM 1001)."""

    ABGELEHNTE_FORDERUNG = "ABGELEHNTE_FORDERUNG"  #: ABGELEHNTE_FORDERUNG
    ZAHLUNGSAVIS = "ZAHLUNGSAVIS"  #: ZAHLUNGSAVIS
