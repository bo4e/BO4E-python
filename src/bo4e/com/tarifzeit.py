"""
Contains Tarifzeit class
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from .. import COM, ComTyp
from ..com.zeitraum import Zeitraum
from ..utils import postprocess_docstring


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
