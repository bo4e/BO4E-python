"""
Übersicht möglicher Anreden, z.B. eines Geschäftspartners.
"""

from enum import Enum

Anrede = Enum(
    "Anrede",
    {
        "HERR": "HERR",
        "FRAU": "FRAU",
        "EHELEUTE": "EHELEUTE",
        "FIRMA": "FIRMA",
        "INDIVIDUELL": "INDIVIDUELL",
    },
)
