"""
Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
"""
from enum import Enum

Energierichtung = Enum("Energierichtung", {"AUSSP": "AUSSP", "EINSP": "EINSP"})  # Ausspeisung  # Einspeisung
