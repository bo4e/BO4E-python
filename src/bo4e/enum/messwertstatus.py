# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Messwertstatus(StrEnum):
    """
    Der Status eines Zählerstandes
    """

    ABGELESEN  #: Abgelesener Wert (abrechnungsrelevant)
    ERSATZWERT  #: Ersatzwert - geschätzt, veranschlagt (abrechnungsrelevant)
    VORSCHLAGSWERT  #: Vorschlagswert (nicht abrechnungsrelevant)
    NICHT_VERWENDBAR  #: Nicht verwendbarer Wert (nicht abrechnungsrelevant)
    PROGNOSEWERT  #: Ein prognostizierter Wert
    VOLAEUFIGERWERT  #: Ein vorläufiger Wert, dieser kann später angepasst werden.
    ENERGIEMENGESUMMIERT  #: Summenwert,  Bilanzsumme
    FEHLT  #: Explizite Kennzeichnung eines fehlenden Wertes
