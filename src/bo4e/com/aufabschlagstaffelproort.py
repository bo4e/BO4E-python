"""
Contains AufAbschlagstaffelProOrt class
"""

from decimal import Decimal
from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class AufAbschlagstaffelProOrt(COM):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/AufAbschlagstaffelProOrt.json>`_

    """

    typ: Annotated[Literal[ComTyp.AUFABSCHLAGSTAFFELPROORT], Field(alias="_typ")] = ComTyp.AUFABSCHLAGSTAFFELPROORT

    wert: Optional[Decimal] = None
    """Der Wert für den Auf- oder Abschlag."""
    staffelgrenze_von: Optional[Decimal] = None
    """Unterer Wert, ab dem die Staffel gilt."""
    staffelgrenze_bis: Optional[Decimal] = None
    """Oberer Wert, bis zu dem die Staffel gilt."""
