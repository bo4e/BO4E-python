# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Bemessungsgroesse(StrEnum):
    """
    Zur Abbildung von Messgrössen und zur Verwendung in energiewirtschaftlichen Berechnungen.
    """

    WIRKARBEIT_EL  #: elektrische Wirkarbeit
    LEISTUNG_EL  #: elektrische Leistung
    BLINDARBEIT_KAP  #: Blindarbeit kapazitiv
    BLINDARBEIT_IND  #: Blindarbeit induktiv
    BLINDLEISTUNG_KAP  #: Blindleistung kapazitiv
    BLINDLEISTUNG_IND  #: Blindleistung induktiv
    WIRKARBEIT_TH  #: thermische Wirkarbeit
    LEISTUNG_TH  #: thermische Leistung
    VOLUMEN  #: Volumen
    VOLUMENSTROM  #: Volumenstrom (Volumen/Zeit)
    BENUTZUNGSDAUER  #: Benutzungsdauer (Arbeit/Leistung)
    ANZAHL  #: Darstellung einer Stückzahl
