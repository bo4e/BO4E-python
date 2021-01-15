"""
Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
"""
from enum import Enum

_energierichtung = {
    "AUSSP": "AUSSP",  # Ausspeisung
    "EINSP": "EINSP"  # Einspeisung
}
Energierichtung = Enum("Energierichtung", _energierichtung)
