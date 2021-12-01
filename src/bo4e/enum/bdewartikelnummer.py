# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class BDEWArtikelnummer(StrEnum):
    """
    BDEW Artikelnummern
    """

    LEISTUNG = "LEISTUNG"  #: Leistung
    LEISTUNG_PAUSCHAL = "LEISTUNG_PAUSCHAL"  #: Leistung pauschal
    GRUNDPREIS = "GRUNDPREIS"  #: Grundpreis
    REGELENERGIE_ARBEIT = "REGELENERGIE_ARBEIT"  #: Regelenergie Arbeit
    REGELENERGIE_LEISTUNG = "REGELENERGIE_LEISTUNG"  #: Regelenergie Leistung
    NOTSTROMLIEFERUNG_ARBEIT = "NOTSTROMLIEFERUNG_ARBEIT"  #: Notstromlieferung Arbeit
    NOTSTROMLIEFERUNG_LEISTUNG = "NOTSTROMLIEFERUNG_LEISTUNG"  #: Notstromlieferung Leistung
    RESERVENETZKAPAZITAET = "RESERVENETZKAPAZITAET"  #: Reservenetzkapazität
    RESERVELEISTUNG = "RESERVELEISTUNG"  #: Reserveleistung
    ZUSAETZLICHE_ABLESUNG = "ZUSAETZLICHE_ABLESUNG"  #: Zusätzliche Ablesung
    PRUEFGEBUEHREN_AUSSERPLANMAESSIG = "PRUEFGEBUEHREN_AUSSERPLANMAESSIG"  #: Prüfgebühren (außerplanmäßig)
    WIRKARBEIT = "WIRKARBEIT"  #: Wirkarbeit
    SINGULAER_GENUTZTE_BETRIEBSMITTEL = (
        "SINGULAER_GENUTZTE_BETRIEBSMITTEL"  #: singulär genutzte Betriebsmittel (z. B. Trafomiete, Leitungen)
    )
    ABGABE_KWKG = "ABGABE_KWKG"  #: Abgabe KWKG
    ABSCHLAG = "ABSCHLAG"  #: Abschlag
    KONZESSIONSABGABE = "KONZESSIONSABGABE"  #: Konzessionsabgabe
    ENTGELT_FERNAUSLESUNG = "ENTGELT_FERNAUSLESUNG"  #: Entgelt für Fernauslesung
    UNTERMESSUNG = "UNTERMESSUNG"  #: Untermessung
    BLINDMEHRARBEIT = "BLINDMEHRARBEIT"  #: Blindmehrarbeit
    ENTGELT_ABRECHNUNG = "ENTGELT_ABRECHNUNG"  #: Entgelt für Abrechnung
    SPERRKOSTEN = "SPERRKOSTEN"  #: Sperrkosten
    ENTSPERRKOSTEN = "ENTSPERRKOSTEN"  #: Entsperrkosten
    MAHNKOSTEN = "MAHNKOSTEN"  #: Mahnkosten
    MEHR_MINDERMENGEN = "MEHR_MINDERMENGEN"  #: Mehr- und Mindermenge
    INKASSOKOSTEN = "INKASSOKOSTEN"  #: Inkassokosten
    BLINDMEHRLEISTUNG = "BLINDMEHRLEISTUNG"  #: Blindmehrleistung
    ENTGELT_MESSUNG_ABLESUNG = "ENTGELT_MESSUNG_ABLESUNG"  #: Entgelt für Messung und Ablesung
    ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK = (
        "ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK"  #: Entgelt für Einbau, Betrieb und Wartung der Messtechnik
    )
    AUSGLEICHSENERGIE = "AUSGLEICHSENERGIE"  #: Ausgleichsenergie
    ZAEHLEINRICHTUNG = "ZAEHLEINRICHTUNG"  #: Zähleinrichtung
    WANDLER_MENGENUMWERTER = "WANDLER_MENGENUMWERTER"  #: Wandler/Mengenumwerter
    KOMMUNIKATIONSEINRICHTUNG = "KOMMUNIKATIONSEINRICHTUNG"  #: Kommunikationseinrichtung
    TECHNISCHE_STEUEREINRICHTUNG = "TECHNISCHE_STEUEREINRICHTUNG"  #: Technische Steuereinrichtung
    PARAGRAF_19_STROM_NEV_UMLAGE = "PARAGRAF_19_STROM_NEV_UMLAGE"  #: § 19 StromNEV Umlage
    BEFESTIGUNGSEINRICHTUNG = "BEFESTIGUNGSEINRICHTUNG"  #: Befestigungseinrichtung (z. B. Zählertafel)
    OFFSHORE_HAFTUNGSUMLAGE = "OFFSHORE_HAFTUNGSUMLAGE"  #: Offshore-Haftungsumlage
    FIXE_ARBEITSENTGELTKOMPONENTE = "FIXE_ARBEITSENTGELTKOMPONENTE"  #: Fixe Arbeitsentgeltkomponente
    FIXE_LEISTUNGSENTGELTKOMPONENTE = "FIXE_LEISTUNGSENTGELTKOMPONENTE"  #: Fixe Leistungsentgeltkomponente
    UMLAGE_ABSCHALTBARE_LASTEN = "UMLAGE_ABSCHALTBARE_LASTEN"  #: Umlage abschaltbare Lasten
    MEHRMENGE = "MEHRMENGE"  #: Mehrmenge
    MINDERMENGE = "MINDERMENGE"  #: Mindermenge
    ENERGIESTEUER = "ENERGIESTEUER"  #: Energiesteuer
    SMARTMETER_GATEWAY = "SMARTMETER_GATEWAY"  #: Smartmeter-Gateway
    STEUERBOX = "STEUERBOX"  #: Steuerbox
    MSB_INKL_MESSUNG = "MSB_INKL_MESSUNG"  #: Messtellenbetrieb inklusive Messung
    AUSGLEICHSENERGIE_UNTERDECKUNG = "AUSGLEICHSENERGIE_UNTERDECKUNG"  #: AusgleichsenergieUnterdeckung
