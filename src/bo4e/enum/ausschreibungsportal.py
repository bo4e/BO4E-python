# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Ausschreibungsportal(StrEnum):
    """
    Aufzählung der unterstützten Ausschreibungsportale.
    """

    ENPORTAL  #: enPORTAL
    ENERGIE_AGENTUR  #: EnergieAgentur.NRW
    BMWI  #: BMWI-Ausschreibungen
    ENERGIE_HANDELSPLATZ  #: energie-handelsplatz.de
    BUND  #: BUND.DE
    VERA_ONLINE  #: vera_online.de
    ISPEX  #: ispex.de
    ENERGIEMARKTPLATZ  #: energiemarktplatz.de
    EVERGABE  #: evergabe.de
    DTAD  #: dtad.de
