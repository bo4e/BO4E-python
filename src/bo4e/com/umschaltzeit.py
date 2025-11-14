"""
Contains Umschaltzeit class
"""

from datetime import time

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM


@postprocess_docstring
class Umschaltzeit(COM):
    """
    Modelliert eine Umschaltzeit, wann auf ein bestimmtes Register geschaltet werden soll.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Umschaltzeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `Umschaltzeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Umschaltzeit.json>`_

    """

    typ: Annotated[Literal[ComTyp.UMSCHALTZEIT], Field(alias="_typ")] = ComTyp.UMSCHALTZEIT

    umschaltzeit: Optional[time] = None
    """Definiert den Zeitpunkt ab dem auf das Register geschaltet wird, das im Feld `registercode` spezifiziert ist."""
    registercode: Optional[str] = None
    """Ein Code, der ein Register spezifiziert. Typischerweise eine 3-stellige Zeichenkette."""
