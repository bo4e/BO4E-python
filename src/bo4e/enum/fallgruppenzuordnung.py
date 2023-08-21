"""
Contains class Fallgruppenzuordnung
"""

from bo4e.enum.strenum import StrEnum

class Fallgruppenzuordnung(StrEnum):
    """
    Fallgruppenzuordnung nach edi@energy
    """

    GABI_RLMmT = "GABI_RLMmT"  #: RLM mit Tagesband,
    GABI_RLMoT = "GABI_RLMoT"  #: RLM ohne Tagesband,
    GABI_RLMNEV = "GABI_RLMNEV"  #: RLM im Nominierungsersatzverfahren
