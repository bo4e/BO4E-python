"""
Contains class Aggregationsverantwortungs
"""

from bo4e.enum.strenum import StrEnum


class Aggregationsverantwortung(StrEnum):
    """
    Mögliche Qualifier für die Aggregationsverantwortung
    """

    UENB = "UENB"  #: Übertragungsnetzbetreiber
    VNB = "VNB"  #: Verteilnetzbetreiber
