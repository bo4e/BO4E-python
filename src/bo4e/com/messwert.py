"""
Contains Messwert class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.menge import Menge
    from ..enum.messwertstatus import Messwertstatus
    from ..enum.messwertstatuszusatz import Messwertstatuszusatz


@postprocess_docstring
class Messwert(COM):
    """
    Abbildung eines Messwertes mit Stati, Zeitpunkt und Wert.
    """

    typ: Annotated[Literal[ComTyp.MESSWERT], Field(alias="_typ")] = ComTyp.MESSWERT

    messwertstatus: Optional["Messwertstatus"] = None
    """Gibt den Status des Messwerts an."""
    messwertstatuszusatz: Optional["Messwertstatuszusatz"] = None
    """Gibt den Status Zusatz des Messwerts an."""
    zeitpunkt: Optional[pydantic.AwareDatetime] = None
    """Gibt den Zeitpunkt des Messwerts an."""
    wert: Optional["Menge"] = None
    """Gibt die gemessene Menge an."""
