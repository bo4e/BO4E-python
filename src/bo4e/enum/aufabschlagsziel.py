# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class AufAbschlagsziel(StrEnum):
    """
    Der Preis, auf den sich ein Auf- oder Abschlag bezieht.
    """

    ARBEITSPREIS_EINTARIF  #: Auf/Abschlag auf den Arbeitspreis Eintarif
    ARBEITSPREIS_HT  #: Auf/Abschlag auf den Arbeitspreis HT
    ARBEITSPREIS_NT  #: Auf/Abschlag auf den Arbeitspreis NT
    ARBEITSPREIS_HT_NT  #: Auf/Abschlag auf den Arbeitspreis HT und NT
    GRUNDPREIS  #: Auf/Abschlag auf den Grundpreis
    GESAMTPREIS  #: Auf/Abschlag auf den Gesamtpreis
