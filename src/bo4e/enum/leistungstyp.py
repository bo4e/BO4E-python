# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


# pylint:disable=empty-docstring
# no docstring in official docs as of 2021-12-01
class Leistungstyp(StrEnum):
    """ """

    ARBEITSPREIS_WIRKARBEIT = "ARBEITSPREIS_WIRKARBEIT"  #: Arbeitspreis zur Abrechnung der Wirkarbeit
    LEISTUNGSPREIS_WIRKLEISTUNG = "LEISTUNGSPREIS_WIRKLEISTUNG"  #: Leistungspreis zur Abrechnung der Wirkleistung
    ARBEITSPREIS_BLINDARBEIT_IND = (
        "ARBEITSPREIS_BLINDARBEIT_IND"  #: Arbeitspreis zur Abrechnung der Blindarbeit induktiv
    )
    ARBEITSPREIS_BLINDARBEIT_KAP = (
        "ARBEITSPREIS_BLINDARBEIT_KAP"  #: Arbeitspreis zur Abrechnung der Blindarbeit kapazitiv
    )
    GRUNDPREIS = "GRUNDPREIS"  #: Grundpreis (pro Zeiteinheit)
    GRUNDPREIS_ARBEIT = "GRUNDPREIS_ARBEIT"  #: Grundpreis, der auf die Arbeit berechnet wird (bei RLM)
    GRUNDPREIS_LEISTUNG = "GRUNDPREIS_LEISTUNG"  #: Grundpreis, der auf die Leistung berechnet wird (bei RLM)
    MEHRMINDERMENGE = "MEHRMINDERMENGE"  #: Mehr- oder Mindermenge
    MESSSTELLENBETRIEB = "MESSSTELLENBETRIEB"  #: Preis pro Zeiteinheit
    MESSDIENSTLEISTUNG = "MESSDIENSTLEISTUNG"  #: Preis pro Zeiteinheit
    MESSDIENSTLEISTUNG_INKL_MESSUNG = (
        "MESSDIENSTLEISTUNG_INKL_MESSUNG"  #: MDL inklusive der Messung (ab 2017), Preis pro Zeiteinheit
    )
    ABRECHNUNG = "ABRECHNUNG"  #: Preis pro Zeiteinheit
    KONZESSIONS_ABGABE = "KONZESSIONS_ABGABE"  #: Konzessionsabgabe
    KWK_UMLAGE = "KWK_UMLAGE"  #: KWK-Umlage
    OFFSHORE_UMLAGE = "OFFSHORE_UMLAGE"  #: Offshore-Haftungsumlage
    ABLAV_UMLAGE = "ABLAV_UMLAGE"  #: Umlage für abschaltbare Lasten
    SONDERKUNDEN_UMLAGE = "SONDERKUNDEN_UMLAGE"  #: §19 StromNEV Umlage
    REGELENERGIE_UMLAGE = "REGELENERGIE_UMLAGE"  #: Regelenergieumlage
    BILANZIERUNG_UMLAGE = "BILANZIERUNG_UMLAGE"  #: Bilanzierungsumlage
    AUSLESUNG_ZUSAETZLICH = "AUSLESUNG_ZUSAETZLICH"  #: Zusätzliche Auslesung (pro Vorgang)
    ABLESUNG_ZUSAETZLICH = "ABLESUNG_ZUSAETZLICH"  #: Zusätzliche Ablesung (pro Vorgang)
    ABRECHNUNG_ZUSAETZLICH = "ABRECHNUNG_ZUSAETZLICH"  #: Zusätzliche Abresung (pro Vorgang)
    SPERRUNG = "SPERRUNG"  #: Sperrung einer Abnahmestelle
    ENTSPERRUNG = "ENTSPERRUNG"  #: Entsperrung einer Abnahmestelle
    MAHNKOSTEN = "MAHNKOSTEN"  #: Mahnkosten
    INKASSOKOSTEN = "INKASSOKOSTEN"  #: Inkassokosten
    EEG_UMLAGE = "EEG_UMLAGE"  #: EEG-Umlage
    ENERGIESTEUER = "ENERGIESTEUER"  #: Strom- oder Erdgassteuer
    NETZPREIS = "NETZPREIS"  #: Netzpreis
    MESSPREIS = "MESSPREIS"  #: Messpreis
    SONSTIGER_PREIS = "SONSTIGER_PREIS"  #: Sonstiger_Preis
