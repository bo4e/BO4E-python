# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Kundentyp(StrEnum):
    """
    Auflistung der Typen von Endkunden. Daraus kann das Verbrauchsprofil abgeleitet werden.
    """

    GEWERBE = "GEWERBE"  #: Gewerbekunden
    PRIVAT = "PRIVAT"  #: Privatkunden
    LANDWIRT = "LANDWIRT"  #: Landwirte
    SONSTIGE = "SONSTIGE"  #: Sonstige Endkunden
    HAUSHALT = "HAUSHALT"  #: Haushaltskunden
    DIREKTHEIZUNG = "DIREKTHEIZUNG"  #: Direktheizungen
    GEMEINSCHAFT_MFH = "GEMEINSCHAFT_MFH"  #: Gemeinschaftseinrichtungen von MFH
    KIRCHE = "KIRCHE"  #: Kirchen und caritative Einrichtungen
    KWK = "KWK"  #: KWK-Anlagen
    LADESAEULE = "LADESAEULE"  #: Ladesäulen
    BELEUCHTUNG_OEFFENTLICH = "BELEUCHTUNG_OEFFENTLICH"  #: Öffentliche Beleuchtungen
    BELEUCHTUNG_STRASSE = "BELEUCHTUNG_STRASSE"  #: Straßenbeleuchtungen
    SPEICHERHEIZUNG = "SPEICHERHEIZUNG"  #: Speicherheizungen
    UNTERBR_EINRICHTUNG = "UNTERBR_EINRICHTUNG"  #: Unterbrechbare Verbrauchseinrichtungen
    WAERMEPUMPE = "WAERMEPUMPE"  #: Wärmepumpen
