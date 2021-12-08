# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Kundengruppe(StrEnum):
    """
    Kundengruppe für eine Marktlokation (orientiert sich an den Standard-Lastprofilen).
    """

    RLM = "RLM"  #: Kunde mit registrierender Leistungsmessung (kein SLP)
    RLM_KOMMUNAL = "RLM_KOMMUNAL"  #: Kommunale Abnahmestelle leistungsgemessen
    SLP_KOMMUNAL = "SLP_KOMMUNAL"  #: Kommunale Abnahmestelle nicht leistungsgemessen
    SLP_S_G0 = "SLP_S_G0"  #: Gewerbe allgemein
    SLP_S_G1 = "SLP_S_G1"  #: Werktags
    SLP_S_G2 = "SLP_S_G2"  #: Verbrauch in Abendstunden
    SLP_S_G3 = "SLP_S_G3"  #: Gewerbe durchlaufend
    SLP_S_G4 = "SLP_S_G4"  #: Laden, Friseur
    SLP_S_G5 = "SLP_S_G5"  #: Bäckerei mit Backstube
    SLP_S_G6 = "SLP_S_G6"  #: Wochenendbetrieb
    SLP_S_G7 = "SLP_S_G7"  #: Mobilfunksendestation
    SLP_S_L0 = "SLP_S_L0"  #: Landwirtschaft allgemein
    SLP_S_L1 = "SLP_S_L1"  #: Landwirtschaft mit Milchwirtschaft/Nebenerwerbs-Tierzucht
    SLP_S_L2 = "SLP_S_L2"  #: Übrige Landwirtschaftsbetriebe
    SLP_S_H0 = "SLP_S_H0"  #: Haushalt allgemein
    SLP_S_SB = "SLP_S_SB"  #: Straßenbeleuchtung
    SLP_S_HZ = "SLP_S_HZ"  #: Nachtspeicherheizung
    SLP_S_WP = "SLP_S_WP"  #: Wärmepumpe
    SLP_S_EM = "SLP_S_EM"  #: Elektromobilität
    SLP_S_HZ_GEM = "SLP_S_HZ_GEM"  #: Nachtspeicherheizung gemeinsame Messung
    SLP_G_GKO = "SLP_G_GKO"  #: Gebietskörpersch., Kreditinst. u. Versich., Org. o. Erwerbszw. & öff. Einr.
    SLP_G_STANDARD = "SLP_G_STANDARD"  #: Standardkundengruppe für Gas
    SLP_G_GHA = "SLP_G_GHA"  #: Einzelhandel, Großhandel
    SLP_G_GMK = "SLP_G_GMK"  #: Metall, Kfz
    SLP_G_GBD = "SLP_G_GBD"  #: sonst. betr. Dienstleistungen
    SLP_G_GGA = "SLP_G_GGA"  #: Beherbergung
    SLP_G_GBH = "SLP_G_GBH"  #: Gaststätten
    SLP_G_GBA = "SLP_G_GBA"  #: Bäckereien
    SLP_G_GWA = "SLP_G_GWA"  #: Wäschereien
    SLP_G_GGB = "SLP_G_GGB"  #: Gartenbau
    SLP_G_GPD = "SLP_G_GPD"  #: Papier und Druck
    SLP_G_GMF = "SLP_G_GMF"  #: haushaltsähnliche Gewerbebetriebe
    SLP_G_HEF = "SLP_G_HEF"  #: Einfamilienhaushalt
    SLP_G_HMF = "SLP_G_HMF"  #: Mehrfamilienhaushalt
    SLP_G_HKO = "SLP_G_HKO"  #: Kochgas
