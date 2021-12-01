# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Vertragsart(StrEnum):
    """
    Aufzählung der Vertragsarten.
    """

    ENERGIELIEFERVERTRAG = "ENERGIELIEFERVERTRAG"  #: Energieliefervertrag
    NETZNUTZUNGSVERTRAG = "NETZNUTZUNGSVERTRAG"  #: Netznutzungsvertrag
    BILANZIERUNGSVERTRAG = "BILANZIERUNGSVERTRAG"  #: Bilanzierungsvertrag
    MESSSTELLENBETRIEBSVERTRAG = "MESSSTELLENBETRIEBSVERTRAG"  #: Messstellenabetriebsvertrag
    BUENDELVERTRAG = "BUENDELVERTRAG"  #: Bündelvertrag
