"""
Contains Preiszeitreihenwert
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from .zeitraum import Zeitraum
    from .preis import Preis
    from .menge import Menge


@postprocess_docstring
class Preiszeitreihenwert(COM):
    """
    Gibt einen Wert und Preis zu einer Zeitreihe an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preiszeitreihenwert.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preiszeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preiszeitreihenwert.json>`_

    """

    typ: Annotated[Literal[ComTyp.PREISZEITREIHENWERT], Field(alias="_typ")] = ComTyp.PREISZEITREIHENWERT

    zeitraum: Optional["Zeitraum"] = None
    """Zeitraum des Preiszeitreihenwerts"""
    preis: Optional["Preis"] = None
    """Preis des Preiszeitreihenwerts"""
    menge: Optional["Menge"] = None
    """Menge des Preiszeitreihenwerts"""
