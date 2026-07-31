"""
Contains Unterschrift class
"""

from typing import Annotated, Literal

import pydantic
from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Unterschrift(COM):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Unterschrift.svg" type="image/svg+xml"></object>

    .. HINT::
        `Unterschrift JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Unterschrift.json>`_

    """

    typ: Annotated[Literal[ComTyp.UNTERSCHRIFT], Field(alias="_typ")] = ComTyp.UNTERSCHRIFT

    name: str | None = None
    """Name des Unterschreibers"""

    ort: str | None = None
    """Ort, an dem die Unterschrift geleistet wird"""
    datum: pydantic.AwareDatetime | None = None
    """Datum der Unterschrift"""
