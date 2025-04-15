"""
Contains Tarifzeiten class
"""

from typing import List, Optional, Annotated, Literal, TYPE_CHECKING
from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.marktteilnehmer import Marktteilnehmer
    from ..com.tarifzeitenzeitscheibe import TarifzeitenZeitscheibe


@postprocess_docstring
class Tarifzeiten(Geschaeftsobjekt):
    """
    Abbildung von Tarifzeiten, wann welche Preise gelten oder unter welchen Bedingungen.
    """

    typ: Annotated[Optional[Literal[BoTyp.TARIFZEITEN]], Field(alias="_typ")] = BoTyp.TARIFZEITEN
    """Typ des Geschäftsobjekts – default 'TARIFZEITEN'"""

    version: Optional[str] = Field(default=None, alias="_version")
    """Optionales Versionsfeld"""

    marktteilnehmer: Optional["Marktteilnehmer"] = None
    """Optionaler Verweis auf den Anbieter / Marktpartner"""

    zeitscheiben: Optional[List["TarifzeitenZeitscheibe"]] = None
    """Liste von Zeitabschnitten, die tarifliche Regelungen enthalten"""