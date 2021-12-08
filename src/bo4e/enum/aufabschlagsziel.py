# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class AufAbschlagsziel(StrEnum):
    """
    Der Preis, auf den sich ein Auf- oder Abschlag bezieht.
    """

    ARBEITSPREIS_EINTARIF = "ARBEITSPREIS_EINTARIF"  #: Auf-/Abschlag auf den Arbeitspreis Eintarif
    ARBEITSPREIS_HT = "ARBEITSPREIS_HT"  #: Auf-/Abschlag auf den Arbeitspreis HT
    ARBEITSPREIS_NT = "ARBEITSPREIS_NT"  #: Auf-/Abschlag auf den Arbeitspreis NT
    ARBEITSPREIS_HT_NT = "ARBEITSPREIS_HT_NT"  #: Auf-/Abschlag auf den Arbeitspreis HT und NT
    GRUNDPREIS = "GRUNDPREIS"  #: Auf-/Abschlag auf den Grundpreis
    GESAMTPREIS = "GESAMTPREIS"  #: Auf-/Abschlag auf den Gesamtpreis
