"""
Contains Tarifzeiten class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

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

    marktteilnehmer: Optional["Marktteilnehmer"] = None
    """Optionaler Verweis auf den Anbieter / Marktpartner"""

    zeitscheiben: Optional[list["TarifzeitenZeitscheibe"]] = None
    """Liste von Zeitabschnitten, die tarifliche Regelungen enthalten"""
