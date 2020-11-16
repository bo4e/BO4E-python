from enum import Enum


class Energierichtung(str, Enum):
    """
    Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
    """

    AUSSP = "AUSSP"
    EINSP = "EINSP"
