"""
Mit dieser Aufzählung können arithmetische Operationen festgelegt werden.
"""

from enum import Enum

_arithmetische_operation = {
    "ADDITION": "ADDITION",
    "SUBTRAKTION": "SUBTRAKTION",
    "MULTIPLIKATION": "MULTIPLIKATION",
    "DIVISION": "DIVISION",
}
ArithmetischeOperation = Enum("ArithmetischeOperation", _arithmetische_operation)
