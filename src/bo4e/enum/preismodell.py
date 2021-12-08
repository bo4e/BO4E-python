# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Preismodell(StrEnum):
    """
    Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung.
    """

    FESTPREIS = "FESTPREIS"  #: FESTPREIS
    TRANCHE = "TRANCHE"  #: TRANCHE
