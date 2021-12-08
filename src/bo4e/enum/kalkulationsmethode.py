# pylint: disable=missing-module-docstring, line-too-long
from bo4e.enum.strenum import StrEnum


class Kalkulationsmethode(StrEnum):
    """
    Auflistung der verschiedenen Berechnungsmethoden für ein Preisblatt.
    """

    STUFEN = "STUFEN"  #: Stufenmodell, d.h. die Gesamtmenge wird in eine Stufe eingeordnet und für die gesamte Menge gilt der so ermittelte Preis
    ZONEN = "ZONEN"  #: Zonenmodell, d.h. die Gesamtmenge wird auf die Zonen aufgeteilt und für die Teilmengen gilt der jeweilige Preis der Zone.
    VORZONEN_GP = "VORZONEN_GP"  #: Vorzonengrundpreis
    SIGMOID = "SIGMOID"  #: Sigmoidfunktion
    BLINDARBEIT_GT_50_PROZENT = "BLINDARBEIT_GT_50_PROZENT"  #: Blindarbeit oberhalb 50% der Wirkarbeit
    BLINDARBEIT_GT_40_PROZENT = "BLINDARBEIT_GT_40_PROZENT"  #: Blindarbeit oberhalb 40% der Wirkarbeit
    BLINDARBEIT_MIT_FREIMENGE = "BLINDARBEIT_MIT_FREIMENGE"  #: Blindarbeit. Freimenge ist durch cos phi oder prozentualem Anteil der Wirkarbeit angegeben.
    AP_GP_ZONEN = "AP_GP_ZONEN"  #: Arbeits- und Grundpreis gezont
    LP_INSTALL_LEISTUNG = "LP_INSTALL_LEISTUNG"  #: Leistungsentgelt auf Grundlage der installierten Leistung
    AP_TRANSPORT_ODER_VERTEILNETZ = "AP_TRANSPORT_ODER_VERTEILNETZ"  #: AP auf Grundlage Transport- oder Verteilnetz
    AP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID = "AP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID"  #: AP auf Grundlage Transport- oder Verteilnetz, Ortsverteilnetz über Sigmoid
    LP_JAHRESVERBRAUCH = "LP_JAHRESVERBRAUCH"  #: Leistungsentgelt auf Grundlage des Jahresverbrauchs
    LP_TRANSPORT_ODER_VERTEILNETZ = "LP_TRANSPORT_ODER_VERTEILNETZ"  #: LP auf Grundlage Transport- oder Verteilnetz
    LP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID = "LP_TRANSPORT_ODER_VERTEILNETZ_ORTSVERTEILNETZ_SIGMOID"  #: LP auf Grundlage Transport- oder Verteilnetz, Ortsverteilnetz über Sigmoid
    FUNKTIONEN = "FUNKTIONEN"  #: Funktionsbezogene Leistungsermittlung bei Verbräuchen oberhalb der SLP Grenze. (ähnlich Sigmoid)
    VERBRAUCH_UEBER_SLP_GRENZE_FUNKTIONSBEZOGEN_WEITERE_BERECHNUNG_ALS_LGK = "VERBRAUCH_UEBER_SLP_GRENZE_FUNKTIONSBEZOGEN_WEITERE_BERECHNUNG_ALS_LGK"  #: Bei einem Verbrauch über der SLP-Grenze (letzte Staffelgrenze überschritten) erfolgt die Berechnung funktionsbezogen (s.o.) als LGK.
