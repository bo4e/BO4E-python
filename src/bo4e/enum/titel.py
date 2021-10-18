"""
Übersicht möglicher Titel, z.B. eines Geschäftspartners.
"""

from enum import Enum

Titel = Enum(
    "Titel",
    {
        "DR": "DR",  # Doktor*In
        "PROF": "PROF",  # Professor*In
        "PROF_DR": "PROF_DR",  # Professor*In Dr.
    },
)
