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
    Abbildung eines Messwertes mit Status, Zeitpunkt und Wert.
    """

    typ: Annotated[Literal[ComTyp.MESSWERT], Field(alias="_typ")] = ComTyp.MESSWERT

    messwertstatus: Optional["Messwertstatus"] = None
    """"""
    messwertstatuszusatz: Optional["Messwertstatuszusatz"] = None
    """"""
    zeitpunkt: Optional[pydantic.AwareDatetime] = None
    """"""
    wert: Optional["Menge"] = None
    """"""
