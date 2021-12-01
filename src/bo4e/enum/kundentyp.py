# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Kundentyp(StrEnum):
    """ """

    GEWERBE  #: Gewerbekunden
    PRIVAT  #: Privatkunden
    LANDWIRT  #: Landwirte
    SONSTIGE  #: Sonstige Endkunden
    HAUSHALT  #: Haushaltskunden
    DIREKTHEIZUNG  #: Direktheizungen
    GEMEINSCHAFT_MFH  #: Gemeinschaftseinrichtungen von MFH
    KIRCHE  #: Kirchen und caritative Einrichtungen
    KWK  #: KWK-Anlagen
    LADESAEULE  #: Ladesäulen
    BELEUCHTUNG_OEFFENTLICH  #: Öffentliche Beleuchtungen
    BELEUCHTUNG_STRASSE  #: Straßenbeleuchtungen
    SPEICHERHEIZUNG  #: Speicherheizungen
    UNTERBR_EINRICHTUNG  #: Unterbrechbare Verbrauchseinrichtungen
    WAERMEPUMPE  #: Wärmepumpen
