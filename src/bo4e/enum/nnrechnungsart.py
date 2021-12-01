# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class NNRechnungsart(StrEnum):
    """
    Abbildung verschiedener in der INVOIC angegebenen Rechnungsarten.
    """

    HANDELSRECHNUNG  #: Handelsrechnung
    SELBSTAUSGESTELLT  #: Selbst ausgestellte Rechnung, z.B. für Einspeiserechnungen.
