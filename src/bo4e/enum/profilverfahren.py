"""
Contains Enums for Profilverfahren.
"""

from bo4e.enum.strenum import StrEnum


class Profilverfahren(StrEnum):
    """
    Profilverfahren: synthetisch/ analytisch.
    """

    SYNTHETISCH = "SYNTHETISCH"  #: SLP
    ANALYTISCH = "ANALYTISCH"  #: ALP
