"""
Contains Preiszeitreihe
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.preistyp import Preistyp
    from .preiszeitreihenwert import Preiszeitreihenwert


@postprocess_docstring
class Preiszeitreihe(COM):
    """

    Gibt Bezeichnung und Preisart zu einer Preiszeitreihe an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preiszeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preiszeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preiszeitreihe.json>`_

    """

    typ: Annotated[Literal[ComTyp.PREISZEITREIHE], Field(alias="_typ")] = ComTyp.PREISZEITREIHE

    preiszeitreihe_id: str | None = None
    """Identifier der Preiszeitreihe"""
    bezeichnung: str | None = None
    """Bezeichnung der Preiszeitreihe"""
    preistyp: Optional["Preistyp"] = None
    """Angabe des Preistyps"""
    werte: list["Preiszeitreihenwert"] | None = None
    """Liste der Preiszeitreihenwerte, die die Preiszeitreihe bilden"""
