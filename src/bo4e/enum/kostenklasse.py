# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Kostenklasse(StrEnum):
    """
    Kostenklassen bilden die oberste Ebene der verschiedenen Kosten.
    In der Regel werden die Gesamtkosten einer Kostenklasse in einer App berechnet.
    """

    FREMDKOSTEN = "FREMDKOSTEN"  #: Fremdkosten
    BESCHAFFUNG = "BESCHAFFUNG"  #: Beschaffung
    SELBSTKOSTEN = "SELBSTKOSTEN"  #: Selbstkosten
    MARGEN = "MARGEN"  #: Margen
    ENERGIEVERSORGUNGSKOSTEN = "ENERGIEVERSORGUNGSKOSTEN"  #: Energieversorgungskosten
