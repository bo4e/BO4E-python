"""
Mit dieser Aufzählung können arithmetische Operationen festgelegt werden.
"""

from enum import Enum

ArithmetischeOperation = Enum(
    "ArithmetischeOperation",
    {
        "ADDITION": "ADDITION",
        "SUBTRAKTION": "SUBTRAKTION",
        "MULTIPLIKATION": "MULTIPLIKATION",
        "DIVISION": "DIVISION",
    },
)
