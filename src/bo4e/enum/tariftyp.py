# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tariftyp(StrEnum):
    """
    Zur Differenzierung von Grund/Ersatzversorgungstarifen und sonstigen angebotenen Tarifen.
    """

    GRUND_ERSATZVERSORGUNG = "GRUND_ERSATZVERSORGUNG"  #: Grund- und Ersatzversorgung
    GRUNDVERSORGUNG = "GRUNDVERSORGUNG"  #: Grundversorgung
    ERSATZVERSORGUNG = "ERSATZVERSORGUNG"  #: Ersatzversorgung
    SONDERTARIF = "SONDERTARIF"  #: Sondertarif
