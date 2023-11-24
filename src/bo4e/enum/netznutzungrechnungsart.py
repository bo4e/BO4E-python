# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class NetznutzungRechnungsart(StrEnum):
    """
    Abbildung verschiedener in der INVOIC angegebenen Rechnungsarten.
    """

    HANDELSRECHNUNG = "HANDELSRECHNUNG"  #: HANDELSRECHNUNG
    SELBSTAUSGESTELLT = "SELBSTAUSGESTELLT"  #: SELBSTAUSGESTELLT
