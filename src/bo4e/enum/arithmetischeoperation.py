# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class ArithmetischeOperation(StrEnum):
    """
    Mit dieser Aufzählung können arithmetische Operationen festgelegt werden.
    """

    ADDITION  #: Es wird addiert
    SUBTRAKTION  #: Es wird subtrahiert
    MULTIPLIKATION  #: Es wird multipliziert
    DIVISION  #: Es wird dividiert
