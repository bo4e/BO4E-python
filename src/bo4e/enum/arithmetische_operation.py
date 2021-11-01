# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class ArithmetischeOperation(StrEnum):
    """
    Mit dieser Aufzählung können arithmetische Operationen festgelegt werden.
    """

    ADDITION = "ADDITION"
    SUBTRAKTION = "SUBTRAKTION"
    MULTIPLIKATION = "MULTIPLIKATION"
    DIVISION = "DIVISION"
