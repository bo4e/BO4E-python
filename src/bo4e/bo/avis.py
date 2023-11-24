"""Contains class Avis"""
from typing import Annotated, Optional

from pydantic import Field

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.avisposition import Avisposition
from bo4e.com.betrag import Betrag
from bo4e.enum.avistyp import AvisTyp

from ..enum.typ import Typ


class Avis(Geschaeftsobjekt):
    """Avis BO"""

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.AVIS

    avis_nummer: str  #: Eine im Verwendungskontext eindeutige Nummer für das Avis.
    avis_typ: AvisTyp  #: Gibt den Typ des Avis an.
    positionen: list[Avisposition]  #: Avispositionen
    zu_zahlen: Betrag  #: Summenbetrag
