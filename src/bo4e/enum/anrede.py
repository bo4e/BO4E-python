"""
Übersicht möglicher Anreden, z.B. eines Geschäftspartners.
"""

from enum import Enum

_anrede = {
    "HERR": "HERR",
    "FRAU": "FRAU",
    "EHELEUTE": "EHELEUTE",
    "FIRMA": "FIRMA",
    "INDIVIDUELL": "INDIVIDUELL",
}
Anrede = Enum("Anrede", _anrede)
