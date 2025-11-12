"""
Contains Tarifzeit class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.zeitraum import Zeitraum


@postprocess_docstring
class Tarifzeit(COM):
    """
    Tarifzeit mit Zuordnung zu einem Zeitraum und einer optionalen Tarifstufe.
    """

    typ: Annotated[Optional[Literal[ComTyp.TARIFZEIT]], Field(alias="_typ")] = ComTyp.TARIFZEIT
    """Typ der Tarifzeit – default 'TARIFZEIT'"""

    zeitraum: Optional["Zeitraum"] = None
    """Gültigkeitszeitraum der Tarifzeit"""

    tarifstufe: Optional[str] = None
    """Optional: Angabe der Tarifstufe, z. B. HT, NT, ST"""
