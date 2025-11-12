"""
Contains Tarifzeiten class
"""

from typing import Annotated, List, Literal, Optional

from pydantic import Field

from ..bo.marktteilnehmer import Marktteilnehmer
from ..com.tarifzeitenzeitscheibe import TarifzeitenZeitscheibe
from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


@postprocess_docstring
class Tarifzeiten(Geschaeftsobjekt):
    """
    Abbildung von Tarifzeiten, wann welche Preise gelten oder unter welchen Bedingungen.
    """

    typ: Annotated[Optional[Literal[BoTyp.TARIFZEITEN]], Field(alias="_typ")] = BoTyp.TARIFZEITEN
    """Typ des Geschäftsobjekts – default 'TARIFZEITEN'"""

    marktteilnehmer: Optional["Marktteilnehmer"] = None
    """Optionaler Verweis auf den Anbieter / Marktpartner"""

    zeitscheiben: Optional[List["TarifzeitenZeitscheibe"]] = None
    """Liste von Zeitabschnitten, die tarifliche Regelungen enthalten"""
