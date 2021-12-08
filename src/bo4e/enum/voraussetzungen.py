# pylint: disable=missing-module-docstring, line-too-long
from bo4e.enum.strenum import StrEnum


class Voraussetzungen(StrEnum):
    """
    Voraussetzungen, die erfüllt sein müssen, damit dieser Tarif zur Anwendung kommen kann.
    """

    EINZUGSERMAECHTIGUNG = "EINZUGSERMAECHTIGUNG"  #: Einzugsermaechtigung
    ZEITPUNKT = "ZEITPUNKT"  #: Vertrag muss zu einem bestimmten Zeitpunkt noch bestehen
    LIEFERANBINDUNG_EINE = "LIEFERANBINDUNG_EINE"  #: Lieferantenbindung für diese Energieart
    LIEFERANBINDUNG_ALLE = (
        "LIEFERANBINDUNG_ALLE"  #: Lieferantenbindung für alle Energiearten, die der Versorger anbietet
    )
    GEWERBE = "GEWERBE"  #: Gewerbenachweis
    LASTPROFIL = "LASTPROFIL"  #: Kunde muss einem bestimmten Lastprofil zuzuordnen sein
    ZAEHLERTYP_GROESSE = "ZAEHLERTYP_GROESSE"  #: bestimmter Zaehlertyp oder Zaehlergroeße
    AUSSCHLUSS_GROSSVERBRAUCHER = "AUSSCHLUSS_GROSSVERBRAUCHER"  #: Ausschluss von Großverbrauchern wie Industriekunden oder produzierendes Gewerbe
    NEUKUNDE = "NEUKUNDE"  #: Neukunden ohne bisherige Lieferanbindung
    BESTIMMTE_VERTRAGSFORMALITAETEN = "BESTIMMTE_VERTRAGSFORMALITAETEN"  #: bestimmte Vertragsformalitaeten wie z.B. Anmeldeformular muss an bestimmte Adresse versandt werden
    SELBSTABLESUNG = "SELBSTABLESUNG"  #: Selbstablesung durch den Kunden
    ONLINEVORAUSSETZUNG = "ONLINEVORAUSSETZUNG"  #: Onlinevoraussetzung
    MINDESTUMSATZ = (
        "MINDESTUMSATZ"  #: Mindestumsatz in einer bestimmten Zeiteinheit wie z.B. Mindestjahresumsatz 2500 EURO
    )
    ZUSATZPRODUKT = (
        "ZUSATZPRODUKT"  #: Zusatzprodukt zu bereits bestehendem Lieferverhaeltnis beim Versorger in dieser Energieart
    )
    NEUKUNDE_MIT_VORAUSSETZUNGEN = (
        "NEUKUNDE_MIT_VORAUSSETZUNGEN"  #: geworbener Neukunde muss bestimmte Voraussetzungen erfüllen
    )
    DIREKTVERTRIEB = "DIREKTVERTRIEB"  #: Kunde wird durch Direktvertrieb gewonnen
    ANSCHLUSSART = "ANSCHLUSSART"  #: Anlage mit bestimmter Anschlussart wie z.B. Festanschluss
    ANSCHLUSSWERT = "ANSCHLUSSWERT"  #: bestimmte Anschlusswerte wie z. B. mindestens 30 kW
    ALTER_KUNDENANLAGE = (
        "ALTER_KUNDENANLAGE"  #: Alter einer Kundenanlage (z.B. Anlage wurde nach dem 01.01.2005 installiert)
    )
    ANLAGEBESCHAFFENHEIT = (
        "ANLAGEBESCHAFFENHEIT"  #: bestimmte Anlagebeschaffenheit, wie bivalente Energieversorgung, Geräte o.ä.
    )
    BETRIEBSSTUNDENBEGRENZUNG = (
        "BETRIEBSSTUNDENBEGRENZUNG"  #: Betriebsstundenbegrenzung z.B. max 1500h/a oder mindestens 1000h/a
    )
    FREIGABEZEITEN = "FREIGABEZEITEN"  #: vorgeschriebene Freigabezeiten
    FAMILIENSTRUKTUR = (
        "FAMILIENSTRUKTUR"  #: Familienstruktur wie z.B. bestimmte Anzahl Kinder oder Personen im Haushalt oder Eheleute
    )
    MITGLIEDSCHAFT = "MITGLIEDSCHAFT"  #: Mitgliedschaft in bestimmten Vereinen oder Verbaenden
    STAATLICHE_FOERDERUNG = "STAATLICHE_FOERDERUNG"  #: staatliche Foerderung wie z.B. Sozialtarif oder Studentenausweis
    BESONDERE_VERBRAUCHSSTELLE = (
        "BESONDERE_VERBRAUCHSSTELLE"  #: besondere Verbrauchsstellen wie Kirchen, Vereinsgebaeude usw.
    )
    NIEDRIGENERGIE = "NIEDRIGENERGIE"  #: Niedrigenergieaustattung des Hauses
    ORTSTEILE_LIEFERGEBIET = "ORTSTEILE_LIEFERGEBIET"  #: nur für bestimmte Ortsteile in diesem Liefergebiet
    WAERMEBEDARF_ERDGAS = "WAERMEBEDARF_ERDGAS"  #: Wärmebedarf wird nur oder überwiegend mit Erdgas gedeckt
    MAX_ZAEHLER_LIEFERSTELLEN = "MAX_ZAEHLER_LIEFERSTELLEN"  #: beschränkt auf max. Anzahl Zähler oder Abnahmestellen
    LIEFERUNGSBESCHRAENKUNG_GASART = (
        "LIEFERUNGSBESCHRAENKUNG_GASART"  #: Lieferungsbeschraenkung auf bestimmte Gasart, wie H-Gas oder L-Gas
    )
    KOMBI_BONI = (
        "KOMBI_BONI"  #: Kombination von Boni, von denen mindestens einer sehr unwahrscheinlich zu erreichen ist
    )
    ALTVERTRAG = "ALTVERTRAG"  #: nur für Altvertraege, die weiterhin gueltig sind
    VORGESCHRIEBENE_ZUSATZANLAGE = (
        "VORGESCHRIEBENE_ZUSATZANLAGE"  #: vorgeschriebene Zusatzanlage wie z.B. Solaranlage etc.
    )
    MEHRERE_ZAEHLER_ABNAHMESTELLEN = "MEHRERE_ZAEHLER_ABNAHMESTELLEN"  #: mehr als 1 Zaehler oder 1 Abnahmestelle
    BESTIMMTER_ABNAHMEFALL = (
        "BESTIMMTER_ABNAHMEFALL"  #: bestimmter Abnahmefall wie z.B. nur Gemeinschaftsheizungen o.ae.
    )
    ZUSATZMODALITAET = "ZUSATZMODALITAET"  #: Zahlungsmodalitaet wie z.B. halbjaehrliche Zahlungsweise
    NACHWEIS_ZAHLUNGSFAEHIGKEIT = (
        "NACHWEIS_ZAHLUNGSFAEHIGKEIT"  #: Nachweis der Zahlungsfaehigkeit wie z.B. Bonitaetsprüfung
    )
    UMSTELLUNG_ENERGIEART = "UMSTELLUNG_ENERGIEART"  #: Umstellung der Energieart
