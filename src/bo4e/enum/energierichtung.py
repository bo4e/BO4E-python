"""
Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
"""
from enum import Enum

_energierichtung = {"AUSSP": "AUSSP", "EINSP": "EINSP"}  # Ausspeisung  # Einspeisung
Energierichtung = Enum("Energierichtung", _energierichtung)
