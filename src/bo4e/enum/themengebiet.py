# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Themengebiet(StrEnum):
    """
    Über dieses ENUM kann eine thematische Zuordnung, beispielsweise eines Ansprechpartners, vorgenommen werden.
    """

    ALLGEMEINER_INFORMATIONSAUSTAUSCH = "ALLGEMEINER_INFORMATIONSAUSTAUSCH"  #: Allgemeiner Informationsaustausch
    AN_UND_ABMELDUNG = "AN_UND_ABMELDUNG"  #: An- und Abmeldung
    ANSPRECHPARTNER_ALLGEMEIN = "ANSPRECHPARTNER_ALLGEMEIN"  #: Ansprechpartner Allgemein
    ANSPRECHPARTNER_BDEW_DVGW = "ANSPRECHPARTNER_BDEW_DVGW"  #: Ansprechpartner BDEW/DVGW
    ANSPRECHPARTNER_IT_TECHNIK = "ANSPRECHPARTNER_IT_TECHNIK"  #: Ansprechpartner IT/Technik
    BILANZIERUNG = "BILANZIERUNG"  #: Bilanzierung
    BILANZKREISKOORDINATOR = "BILANZKREISKOORDINATOR"  #: Bilanzkreiskoordinator
    BILANZKREISVERANTWORTLICHER = "BILANZKREISVERANTWORTLICHER"  #: Bilanzkreisverantwortlicher
    DATENFORMATE_ZERTIFIKATE_VERSCHLUESSELUNGEN = (
        "DATENFORMATE_ZERTIFIKATE_VERSCHLUESSELUNGEN"  #: Datenformate, Zertifikate, Verschlüsselungen
    )
    DEBITORENMANAGEMENT = "DEBITORENMANAGEMENT"  #: Debitorenmanagement
    DEMAND_SIDE_MANAGEMENT = "DEMAND_SIDE_MANAGEMENT"  #: Demand-Side-Management
    EDI_VEREINBARUNG = "EDI_VEREINBARUNG"  #: EDI-Vereinbarung
    EDIFACT = "EDIFACT"  #: EDIFACT
    ENERGIEDATENMANAGEMENT = "ENERGIEDATENMANAGEMENT"  #: Energiedatenmanagement
    FAHRPLANMANAGEMENT = "FAHRPLANMANAGEMENT"  #: Fahrplanmanagement
    ALOCAT = "ALOCAT"  #: Format:ALOCAT
    APERAK = "APERAK"  #: Format:APERAK
    CONTRL = "CONTRL"  #: Format:CONTRL
    INVOIC = "INVOIC"  #: Format:INVOIC
    MSCONS = "MSCONS"  #: Format:MSCONS
    ORDERS = "ORDERS"  #: Format:ORDERS
    ORDERSP = "ORDERSP"  #: Format:ORDERSP
    REMADV = "REMADV"  #: Format:REMADV
    UTILMD = "UTILMD"  #: Format:UTILMD
    GABI = "GABI"  #: GaBi Gas
    GELI = "GELI"  #: GeLi Gas
    GERAETERUECKGABE = "GERAETERUECKGABE"  #: Geräterückgabe
    GERAETEWECHSEL = "GERAETEWECHSEL"  #: Gerätewechsel
    GPKE = "GPKE"  #: GPKE
    INBETRIEBNAHME = "INBETRIEBNAHME"  #: Inbetriebnahme
    KAPAZITAETSMANAGEMENT = "KAPAZITAETSMANAGEMENT"  #: Kapazitätsmanagement
    KLAERFAELLE = "KLAERFAELLE"  #: Klärfälle
    LASTGAENGE_RLM = "LASTGAENGE_RLM"  #: Lastgänge RLM
    LIEFERANTENRAHMENVERTRAG = "LIEFERANTENRAHMENVERTRAG"  #: Lieferantenrahmenvertrag
    LIEFERANTENWECHSEL = "LIEFERANTENWECHSEL"  #: Lieferantenwechsel
    MABIS = "MABIS"  #: MaBiS
    MAHNWESEN = "MAHNWESEN"  #: Mahnwesen
    MARKTGEBIETSVERANTWORTLICHER = "MARKTGEBIETSVERANTWORTLICHER"  #: Marktgebietsverantwortlicher
    MARKTKOMMUNIKATION = "MARKTKOMMUNIKATION"  #: Marktkommunikation
    MEHR_MINDERMENGEN = "MEHR_MINDERMENGEN"  #: Mehr- Mindermengen
    MSB_MDL = "MSB_MDL"  #: MSB - MDL
    NETZABRECHNUNG = "NETZABRECHNUNG"  #: Netzabrechnung
    NETZENTGELTE = "NETZENTGELTE"  #: Netzentgelte
    NETZMANAGEMENT = "NETZMANAGEMENT"  #: Netzmanagement
    RECHT = "RECHT"  #: Recht
    REGULIERUNGSMANAGEMENT = "REGULIERUNGSMANAGEMENT"  #: Regulierungsmanagement
    REKLAMATIONEN = "REKLAMATIONEN"  #: Reklamationen
    SPERREN_ENTSPERREN_INKASSO = "SPERREN_ENTSPERREN_INKASSO"  #: Sperren/Entsperren/Inkasso
    STAMMDATEN = "STAMMDATEN"  #: Stammdaten
    STOERUNGSFAELLE = "STOERUNGSFAELLE"  #: Übermittlung_Störungsfälle
    TECHNISCHE_FRAGEN = "TECHNISCHE_FRAGEN"  #: Technische Fragen
    UMSTELLUNG_INVOIC = "UMSTELLUNG_INVOIC"  #: Umstellung INVOIC
    VERSCHLUESSELUNG_SIGNATUR = "VERSCHLUESSELUNG_SIGNATUR"  #: Verschlüsselung/Signatur
    VERTRAGSMANAGEMENT = "VERTRAGSMANAGEMENT"  #: Vertragsmanagement
    VERTRIEB = "VERTRIEB"  #: Vertrieb
    WIM = "WIM"  #: WiM
    ZAEHLERSTAENDE_SLP = "ZAEHLERSTAENDE_SLP"  #: Zählerstände SLP
    ZAHLUNGSVERKEHR = "ZAHLUNGSVERKEHR"  #: Zahlungsverkehr
    ZUORDNUNGSVEREINBARUNG = "ZUORDNUNGSVEREINBARUNG"  #: Zuordnungsvereinbarung
