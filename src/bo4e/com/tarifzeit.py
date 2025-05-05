"""
Contains Tarifzeit class
"""

from typing import Optional, Annotated, Literal
from pydantic import Field

from .. import COM, ComTyp
from ..utils import postprocess_docstring
from ..com.zeitraum import Zeitraum


@postprocess_docstring
class Tarifzeit(COM):
    """
    Tarifzeit mit Zuordnung zu einem Zeitraum und einer optionalen Tarifstufe.
    """

    typ: Annotated[Optional[Literal[ComTyp.TARIFZEIT]], Field(alias="_typ")] = ComTyp.TARIFZEIT
    """Typ der Tarifzeit – default 'TARIFZEIT'"""

    zeitraum: Optional[Zeitraum] = None
    """Gültigkeitszeitraum der Tarifzeit"""

    tarifstufe: Optional[str] = None
    """Optional: Angabe der Tarifstufe, z. B. HT, NT, ST"""
