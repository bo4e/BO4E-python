# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class SteuerkanalLeistungsbeschreibung(StrEnum):
    """
    Beschreibung des Steuerkanals
    """

    AN_AUS = "AN_AUS"
    GESTUFT = "GESTUFT"
