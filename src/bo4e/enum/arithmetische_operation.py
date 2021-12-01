# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class ArithmetischeOperation(StrEnum):
    """
    Mit dieser Aufzählung können arithmetische Operationen festgelegt werden.
    """

    ADDITION = "ADDITION"  #: Es wird addiert
    SUBTRAKTION = "SUBTRAKTION"  #: Es wird subtrahiert
    MULTIPLIKATION = "MULTIPLIKATION"  #: Es wird multipliziert
    DIVISION = "DIVISION"  #: Es wird dividiert
