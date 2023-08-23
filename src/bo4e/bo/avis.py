"""Contains class Avis"""
from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.avisposition import Avisposition
from bo4e.com.betrag import Betrag
from bo4e.enum.avistyp import AvisTyp
from bo4e.enum.botyp import BoTyp


class Avis(Geschaeftsobjekt):
    """Avis BO"""

    bo_typ: BoTyp = BoTyp.AVIS  # added to botyp.py

    #: required attributes
    avis_nummer: str  #: Eine im Verwendungskontext eindeutige Nummer für das Avis.
    avis_typ: AvisTyp  #: Gibt den Typ des Avis an.
    positionen: list[Avisposition]  #: Avispositionen
    zu_zahlen: Betrag  #: Summenbetrag
