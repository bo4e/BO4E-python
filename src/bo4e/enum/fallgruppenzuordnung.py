"""
Contains Enums for Fallgruppenzuordnung
"""

from bo4e.enum.strenum import StrEnum


class Fallgruppenzuordnung(StrEnum):
    """
    Fallgruppenzuordnung nach edi@energy
    """

    GABI_RLM_MIT_TAGESBAND = "GABI_RLM_MIT_TAGESBAND"
    """RLM mit Tagesband"""
    GABI_RLM_OHNE_TAGESBAND = "GABI_RLM_OHNE_TAGESBAND"
    """RLM ohne Tagesband"""
    GABI_RLM_IM_NOMINIERUNGSERSATZVERFAHREN = "GABI_RLM_IM_NOMINIERUNGSERSATZVERFAHREN"
    """RLM im Nominierungsersatzverfahren"""
