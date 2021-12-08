# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Preistyp(StrEnum):
    """
    Aufschlüsselung der Preistypen in Tarifen.
    """

    GRUNDPREIS = "GRUNDPREIS"  #: Grundpreis
    ARBEITSPREIS_EINTARIF = "ARBEITSPREIS_EINTARIF"  #: Arbeitspreis_ET
    ARBEITSPREIS_HT = "ARBEITSPREIS_HT"  #: Arbeitspreis_HT
    ARBEITSPREIS_NT = "ARBEITSPREIS_NT"  #: Arbeitspreis_NT
    LEISTUNGSPREIS = "LEISTUNGSPREIS"  #: Leistungspreis
    MESSPREIS = "MESSPREIS"  #: Messpreis
    ENTGELT_ABLESUNG = "ENTGELT_ABLESUNG"  #: Entgelt fuer Ablesung
    ENTGELT_ABRECHNUNG = "ENTGELT_ABRECHNUNG"  #: Entgelt fuer Abrechnung
    ENTGELT_MSB = "ENTGELT_MSB"  #: Entgelt für MSB (Entgelt für Einbau, Betrieb und Wartung der Messtechnik)
    PROVISION = "PROVISION"  #: Provision
