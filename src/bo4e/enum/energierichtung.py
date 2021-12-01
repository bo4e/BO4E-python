# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Energierichtung(StrEnum):
    """
    Spezifiziert die Energierichtung einer Markt- und/oder Messlokation
    """

    AUSSP = "AUSSP"  #: Ausspeisung
    EINSP = "EINSP"  #: Einspeisung
