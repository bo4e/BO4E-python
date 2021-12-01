# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class BDEWArtikelnummer(StrEnum):
    """
    BezeichnungbdewArtikelnummerNameLEISTUNG9990001000053LeistungLEISTUNG_PAUSCHAL9990001000079Leistung pauschalGRUNDPREIS9990001000087GrundpreisREGELENERGIE_ARBEIT9990001000128Regelenergie ArbeitREGELENERGIE_LEISTUNG9990001000136Regelenergie LeistungNOTSTROMLIEFERUNG_ARBEIT9990001000144Notstromlieferung ArbeitNOTSTROMLIEFERUNG_LEISTUNG9990001000152Notstromlieferung LeistungRESERVENETZKAPAZITAET9990001000160ReservenetzkapazitätRESERVELEISTUNG9990001000178ReserveleistungZUSAETZLICHE_ABLESUNG9990001000186Zusätzliche AblesungPRUEFGEBUEHREN_AUSSERPLANMAESSIG9990001000219Prüfgebühren (außerplanmäßig)WIRKARBEIT9990001000269WirkarbeitSINGULAER_GENUTZTE_BETRIEBSMITTEL9990001000285singulär genutzte Betriebsmittel (z
    """

    LEISTUNG  #: Leistung
    LEISTUNG_PAUSCHAL  #: Leistung pauschal
    GRUNDPREIS  #: Grundpreis
    REGELENERGIE_ARBEIT  #: Regelenergie Arbeit
    REGELENERGIE_LEISTUNG  #: Regelenergie Leistung
    NOTSTROMLIEFERUNG_ARBEIT  #: Notstromlieferung Arbeit
    NOTSTROMLIEFERUNG_LEISTUNG  #: Notstromlieferung Leistung
    RESERVENETZKAPAZITAET  #: Reservenetzkapazität
    RESERVELEISTUNG  #: Reserveleistung
    ZUSAETZLICHE_ABLESUNG  #: Zusätzliche Ablesung
    PRUEFGEBUEHREN_AUSSERPLANMAESSIG  #: Prüfgebühren (außerplanmäßig)
    WIRKARBEIT  #: Wirkarbeit
    SINGULAER_GENUTZTE_BETRIEBSMITTEL  #: singulär genutzte Betriebsmittel (z. B. Trafomiete, Leitungen)
    ABGABE_KWKG  #: Abgabe KWKG
    ABSCHLAG  #: Abschlag
    KONZESSIONSABGABE  #: Konzessionsabgabe
    ENTGELT_FERNAUSLESUNG  #: Entgelt für Fernauslesung
    UNTERMESSUNG  #: Untermessung
    BLINDMEHRARBEIT  #: Blindmehrarbeit
    ENTGELT_ABRECHNUNG  #: Entgelt für Abrechnung
    SPERRKOSTEN  #: Sperrkosten
    ENTSPERRKOSTEN  #: Entsperrkosten
    MAHNKOSTEN  #: Mahnkosten
    MEHR_MINDERMENGEN  #: Mehr- und Mindermenge
    INKASSOKOSTEN  #: Inkassokosten
    BLINDMEHRLEISTUNG  #: Blindmehrleistung
    ENTGELT_MESSUNG_ABLESUNG  #: Entgelt für Messung und Ablesung
    ENTGELT_EINBAU_BETRIEB_WARTUNG_MESSTECHNIK  #: Entgelt für Einbau, Betrieb und Wartung der Messtechnik
    AUSGLEICHSENERGIE  #: Ausgleichsenergie
    ZAEHLEINRICHTUNG  #: Zähleinrichtung
    WANDLER_MENGENUMWERTER  #: Wandler/Mengenumwerter
    KOMMUNIKATIONSEINRICHTUNG  #: Kommunikationseinrichtung
    TECHNISCHE_STEUEREINRICHTUNG  #: Technische Steuereinrichtung
    PARAGRAF_19_STROM_NEV_UMLAGE  #: § 19 StromNEV Umlage
    BEFESTIGUNGSEINRICHTUNG  #: Befestigungseinrichtung (z. B. Zählertafel)
    OFFSHORE_HAFTUNGSUMLAGE  #: Offshore-Haftungsumlage
    FIXE_ARBEITSENTGELTKOMPONENTE  #: Fixe Arbeitsentgeltkomponente
    FIXE_LEISTUNGSENTGELTKOMPONENTE  #: Fixe Leistungsentgeltkomponente
    UMLAGE_ABSCHALTBARE_LASTEN  #: Umlage abschaltbare Lasten
    MEHRMENGE  #: Mehrmenge
    MINDERMENGE  #: Mindermenge
    ENERGIESTEUER  #: Energiesteuer
    SMARTMETER_GATEWAY  #: Smartmeter-Gateway
    STEUERBOX  #: Steuerbox
    MSB_INKL_MESSUNG  #: Messtellenbetrieb inklusive Messung
    AUSGLEICHSENERGIE_UNTERDECKUNG  #: AusgleichsenergieUnterdeckung
