"""
Contains KriteriumWert class
"""

# pylint: disable=too-few-public-methods
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.tarifregionskriterium import Tarifregionskriterium


@postprocess_docstring
class KriteriumWert(COM):
    """
    Mit dieser Komponente können Kriterien und deren Werte definiert werden

    .. raw:: html

        <object data="../_static/images/bo4e/com/KriteriumWert.svg" type="image/svg+xml"></object>

    .. HINT::
        `KriteriumWert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/KriteriumWert.json>`_

    """

    typ: Annotated[Literal[ComTyp.KRITERIUMWERT], Field(alias="_typ")] = ComTyp.KRITERIUMWERT

    kriterium: Optional["Tarifregionskriterium"] = None
    """Hier steht, für welches Kriterium der Wert gilt. Z.B. Postleitzahlen"""
    wert: Optional[str] = None
    """Ein Wert, passend zum Kriterium. Z.B. eine Postleitzahl."""
