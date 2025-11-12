"""
Contains Tarifzeitstufe class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.zeitraum import Zeitraum


@postprocess_docstring
class Tarifzeitstufe(COM):
    """
    Tarifzeitstufe mit Zuordnung zu einem Zeitraum und einer optionalen Tarifstufe.
    """

    typ: Annotated[Optional[Literal[ComTyp.TARIFZEITSTUFE]], Field(alias="_typ")] = ComTyp.TARIFZEITSTUFE
    """Typ der Tarifzeitstufe – default 'TARIFZEITSTUFE'"""

    zeitraum: Optional["Zeitraum"] = None
    """Gültigkeitszeitraum der Tarifzeitstufe"""

    tarifstufe: Optional[str] = None
    """Optional: Angabe der Tarifstufe, z. B. HT, NT, ST"""
