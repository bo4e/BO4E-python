"""
Übersicht möglicher Titel, z.B. eines Geschäftspartners.
"""

from enum import Enum

_titel = {
    "DR": "DR",  # Doktor
    "PROF": "PROF",  # Professor
    "PROF-DR": "PROF-DR",  # Professor Dr.
}
Titel = Enum("Titel", _titel)
