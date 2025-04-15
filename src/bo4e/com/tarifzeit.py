from typing import Optional, Annotated, Literal, TYPE_CHECKING
from pydantic import Field

from .. import COM, ComTyp
from ..utils import postprocess_docstring

if TYPE_CHECKING:
    from ..com.zeitraum import Zeitraum
    from ..enum.tarifstufen import Tarifstufen


@postprocess_docstring
class Tarifzeit(COM):
    """
    Tarifzeit mit Zuordnung zu einem Zeitraum und einer optionalen Tarifstufe.
    """

    typ: Annotated[Optional[Literal[ComTyp.TARIFZEIT]], Field(alias="_typ")] = ComTyp.TARIFZEIT
    """Typ der Tarifzeit – default 'TARIFZEIT'"""

    zeitraum: Optional["Zeitraum"] = None
    """Gültigkeitszeitraum der Tarifzeit"""

    tarifstufe: Optional[Tarifstufen] = None
    """Optional: Angabe der Tarifstufe, z. B. HT, NT, ST"""
