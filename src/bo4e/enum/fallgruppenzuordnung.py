"""
Contains class Fallgruppenzuordnung
"""

from bo4e.enum.strenum import StrEnum


class Fallgruppenzuordnung(StrEnum):
    """
    Fallgruppenzuordnung nach edi@energy
    """

    # todo: Uppercase-Problematik klären. -> pylint
    GABI_RLMmT = "GABI_RLMmT"  # pylint:disable=invalid-name
    # #: RLM mit Tagesband,
    GABI_RLMoT = "GABI_RLMoT"  # pylint:disable=invalid-name
    # #: RLM ohne Tagesband,
    GABI_RLMNEV = "GABI_RLMNEV"
    #: RLM im Nominierungsersatzverfahren
