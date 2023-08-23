"""Contains Class: Abweichung."""
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.abweichungsgrund import Abweichungsgrund


class Abweichung(COM):
    """Zur Angabe einer Abweichung bei Ablehnung einer COMDIS. (REMADV SG5 RFF und SG7 AJT/FTX)."""

    # optional attributes
    abweichungsgrund: Optional[Abweichungsgrund] = None  #: Angabe Abweichungsgrund
    abweichungsgrund_bemerkung: Optional[str] = None  #: Nähere Erläuterung zum Abweichungsgrund
    zugehoerige_rechnung: Optional[str] = None  #: Zugehoerige Rechnung
    abschlagsrechnung: Optional[str] = None  #: Abschlagsrechnung
    abweichungsgrund_code: Optional[str] = None  #: Angabe Abweichungsgrund(Code)
    abweichungsgrund_codeliste: Optional[str] = None  #: Angabe Abweichungsgrund(Codeliste)
