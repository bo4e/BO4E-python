# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Operator(StrEnum):
    """
    Mit dieser Aufzählung können Operationen festgelegt werden.
    """

    ADDITION = "ADDITION"
    """Es wird addiert"""
    SUBTRAKTION = "SUBTRAKTION"
    """Es wird subtrahiert"""
    MULTIPLIKATION = "MULTIPLIKATION"
    """Es wird multipliziert"""
    DIVISION = "DIVISION"
    """Es wird dividiert"""
