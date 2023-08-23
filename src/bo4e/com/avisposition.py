"""Contains class Avisposition"""
from datetime import datetime
from typing import Optional

from bo4e.com.abweichung import Abweichung
from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.rueckmeldungsposition import Rueckmeldungsposition


class Avisposition(COM):
    """Die Position eines Avis"""

    # required attributes
    rechnungs_nummer: str  #: Die Rechnungsnummer der Rechnung, auf welche sich das Avis bezieht.
    rechnungs_datum: datetime  #: Das Rechnungsdatum der Rechnung, auf die sich das Avis bezieht.
    ist_storno: bool
    #:  Kennzeichnung, ob es sich bei der Rechnung auf die sich das Avis bezieht, um eine Stornorechnung handelt.
    gesamtbrutto: Betrag  #: Überweisungsbetrag
    zu_zahlen: Betrag  #: Geforderter Rechnungsbetrag

    # optional attributes
    ist_selbstausgestellt: Optional[bool] = None
    #: Kennzeichnung, ob es sich bei der Rechnung auf die sich das Avis bezieht, um eine Stornorechnung handelt.
    referenz: Optional[str] = None  #: Referenzierung auf eine vorherige COMDIS-Nachricht
    abweichungen: Optional[list[Abweichung]] = None  #: Abweichungen bei Ablehnung einer COMDIS
    positionen: Optional[list[Rueckmeldungsposition]] = None  #: Rückmeldungspositionen
