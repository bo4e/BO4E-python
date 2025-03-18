"""Contains class Abweichungsposition."""
from typing import Optional

from bo4e.com.com import COM


class Abweichungsposition(COM):
    """Zur Angabe einer Abweichung einer einzelnen Position."""

    abweichungsgrund_code: Optional[str] = None  #: Angabe Abweichungsgrund(Code)
    abweichungsgrund_codeliste: Optional[str] = None  #:Angabe Abweichungsgrund(Codeliste)
    abweichungsgrund_bemerkung: Optional[str] = None  #: Nähere Erläuterung zum Abweichungsgrund
    zugehoerige_rechnung: Optional[str] = None  #: Zugehörige Rechnung
    zugehoerige_bestellung: Optional[str] = None  #: Zugehörige Bestellung
