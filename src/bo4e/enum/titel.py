"""
Übersicht möglicher Titel, z.B. eines Geschäftspartners.
"""

from enum import Enum

_titel = {
    "DR": "DR",
    "PROF": "PROF",
    "PROF-DR": "PROF-DR",
}
Titel = Enum("Titel", _titel)
