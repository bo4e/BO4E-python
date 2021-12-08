# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Ausschreibungsportal(StrEnum):
    """
    Aufzählung der unterstützten Ausschreibungsportale.
    """

    ENPORTAL = "ENPORTAL"  #: enPORTAL
    ENERGIE_AGENTUR = "ENERGIE_AGENTUR"  #: EnergieAgentur.NRW
    BMWI = "BMWI"  #: BMWI-Ausschreibungen
    ENERGIE_HANDELSPLATZ = "ENERGIE_HANDELSPLATZ"  #: energie-handelsplatz.de
    BUND = "BUND"  #: BUND.DE
    VERA_ONLINE = "VERA_ONLINE"  #: vera_online.de
    ISPEX = "ISPEX"  #: ispex.de
    ENERGIEMARKTPLATZ = "ENERGIEMARKTPLATZ"  #: energiemarktplatz.de
    EVERGABE = "EVERGABE"  #: evergabe.de
    DTAD = "DTAD"  #: dtad.de
