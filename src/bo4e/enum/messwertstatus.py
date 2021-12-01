# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messwertstatus(StrEnum):
    """
    Der Status eines Zählerstandes
    """

    ABGELESEN = "ABGELESEN"  #: ABGELESEN
    ERSATZWERT = "ERSATZWERT"  #: ERSATZWERT
    VORSCHLAGSWERT = "VORSCHLAGSWERT"  #: VORSCHLAGSWERT
    NICHT_VERWENDBAR = "NICHT_VERWENDBAR"  #: NICHT_VERWENDBAR
    PROGNOSEWERT = "PROGNOSEWERT"  #: PROGNOSEWERT
    VOLAEUFIGERWERT = "VOLAEUFIGERWERT"  #: VOLAEUFIGERWERT
    ENERGIEMENGESUMMIERT = "ENERGIEMENGESUMMIERT"  #: ENERGIEMENGESUMMIERT
    FEHLT = "FEHLT"  #: FEHLT
