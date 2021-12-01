# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Leistungstyp(StrEnum):
    """
    BezeichnungNameARBEITSPREIS_WIRKARBEITArbeitspreis zur Abrechnung der WirkarbeitLEISTUNGSPREIS_WIRKLEISTUNGLeistungspreis zur Abrechnung der WirkleistungARBEITSPREIS_BLINDARBEIT_INDArbeitspreis zur Abrechnung der Blindarbeit induktivARBEITSPREIS_BLINDARBEIT_KAPArbeitspreis zur Abrechnung der Blindarbeit kapazitivGRUNDPREISGrundpreis (pro Zeiteinheit)GRUNDPREIS_ARBEITGrundpreis, der auf die Arbeit berechnet wird (bei RLM)GRUNDPREIS_LEISTUNGGrundpreis, der auf die Leistung berechnet wird (bei RLM)MEHRMINDERMENGEMehr- oder MindermengeMESSSTELLENBETRIEBPreis pro ZeiteinheitMESSDIENSTLEISTUNGPreis pro ZeiteinheitMESSDIENSTLEISTUNG_INKL_MESSUNGMDL inklusive der Messung (ab 2017), Preis pro ZeiteinheitABRECHNUNGPreis pro ZeiteinheitKONZESSIONS_ABGABEKonzessionsabgabeKWK_UMLAGEKWK-UmlageOFFSHORE_UMLAGEOffshore-HaftungsumlageABLAV_UMLAGEUmlage für abschaltbare LastenSONDERKUNDEN_UMLAGE§19 StromNEV UmlageREGELENERGIE_UMLAGERegelenergieumlageBILANZIERUNG_UMLAGEBilanzierungsumlageAUSLESUNG_ZUSAETZLICHZusätzliche Auslesung (pro Vorgang)ABLESUNG_ZUSAETZLICHZusätzliche Ablesung (pro Vorgang)ABRECHNUNG_ZUSAETZLICHZusätzliche Abresung (pro Vorgang)SPERRUNGSperrung einer AbnahmestelleENTSPERRUNGEntsperrung einer AbnahmestelleMAHNKOSTENMahnkostenINKASSOKOSTENInkassokostenEEG_UMLAGEEEG-UmlageENERGIESTEUERStrom- oder ErdgassteuerNETZPREISNetzpreisMESSPREISMesspreisSONSTIGER_PREISSonstiger_Preis
    """

    ARBEITSPREIS_WIRKARBEIT  #: Arbeitspreis zur Abrechnung der Wirkarbeit
    LEISTUNGSPREIS_WIRKLEISTUNG  #: Leistungspreis zur Abrechnung der Wirkleistung
    ARBEITSPREIS_BLINDARBEIT_IND  #: Arbeitspreis zur Abrechnung der Blindarbeit induktiv
    ARBEITSPREIS_BLINDARBEIT_KAP  #: Arbeitspreis zur Abrechnung der Blindarbeit kapazitiv
    GRUNDPREIS  #: Grundpreis (pro Zeiteinheit)
    GRUNDPREIS_ARBEIT  #: Grundpreis, der auf die Arbeit berechnet wird (bei RLM)
    GRUNDPREIS_LEISTUNG  #: Grundpreis, der auf die Leistung berechnet wird (bei RLM)
    MEHRMINDERMENGE  #: Mehr- oder Mindermenge
    MESSSTELLENBETRIEB  #: Preis pro Zeiteinheit
    MESSDIENSTLEISTUNG  #: Preis pro Zeiteinheit
    MESSDIENSTLEISTUNG_INKL_MESSUNG  #: MDL inklusive der Messung (ab 2017), Preis pro Zeiteinheit
    ABRECHNUNG  #: Preis pro Zeiteinheit
    KONZESSIONS_ABGABE  #: Konzessionsabgabe
    KWK_UMLAGE  #: KWK-Umlage
    OFFSHORE_UMLAGE  #: Offshore-Haftungsumlage
    ABLAV_UMLAGE  #: Umlage für abschaltbare Lasten
    SONDERKUNDEN_UMLAGE  #: §19 StromNEV Umlage
    REGELENERGIE_UMLAGE  #: Regelenergieumlage
    BILANZIERUNG_UMLAGE  #: Bilanzierungsumlage
    AUSLESUNG_ZUSAETZLICH  #: Zusätzliche Auslesung (pro Vorgang)
    ABLESUNG_ZUSAETZLICH  #: Zusätzliche Ablesung (pro Vorgang)
    ABRECHNUNG_ZUSAETZLICH  #: Zusätzliche Abresung (pro Vorgang)
    SPERRUNG  #: Sperrung einer Abnahmestelle
    ENTSPERRUNG  #: Entsperrung einer Abnahmestelle
    MAHNKOSTEN  #: Mahnkosten
    INKASSOKOSTEN  #: Inkassokosten
    EEG_UMLAGE  #: EEG-Umlage
    ENERGIESTEUER  #: Strom- oder Erdgassteuer
    NETZPREIS  #: Netzpreis
    MESSPREIS  #: Messpreis
    SONSTIGER_PREIS  #: Sonstiger_Preis
