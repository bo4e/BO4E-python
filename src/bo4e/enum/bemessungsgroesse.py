# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Bemessungsgroesse(StrEnum):
    """
    Zur Abbildung von Messgrössen und zur Verwendung in energiewirtschaftlichen Berechnungen.
    """

    WIRKARBEIT_EL = "WIRKARBEIT_EL"  #: elektrische Wirkarbeit
    LEISTUNG_EL = "LEISTUNG_EL"  #: elektrische Leistung
    BLINDARBEIT_KAP = "BLINDARBEIT_KAP"  #: Blindarbeit kapazitiv
    BLINDARBEIT_IND = "BLINDARBEIT_IND"  #: Blindarbeit induktiv
    BLINDLEISTUNG_KAP = "BLINDLEISTUNG_KAP"  #: Blindleistung kapazitiv
    BLINDLEISTUNG_IND = "BLINDLEISTUNG_IND"  #: Blindleistung induktiv
    WIRKARBEIT_TH = "WIRKARBEIT_TH"  #: thermische Wirkarbeit
    LEISTUNG_TH = "LEISTUNG_TH"  #: thermische Leistung
    VOLUMEN = "VOLUMEN"  #: Volumen
    VOLUMENSTROM = "VOLUMENSTROM"  #: Volumenstrom (Volumen/Zeit)
    BENUTZUNGSDAUER = "BENUTZUNGSDAUER"  #: Benutzungsdauer (Arbeit/Leistung)
    ANZAHL = "ANZAHL"  #: Darstellung einer Stückzahl
