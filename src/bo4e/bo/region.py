"""
Contains Region class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.regionsoperation import Regionsoperation


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Liste von Regionsoperationen.

    Die Reihenfolge der Regionsoperationen ist relevant,
    wird aber nicht zwingend durch die Sortierung innerhalb der Liste definiert. Die Sortierung der Regionsoperationen
    wird durch das Feld `prioritaet` im COM `Regionsoperation` explizit festgelegt, um technischen Problemen bei
    spezifischen Umsetzungen vorzubeugen und Klarheit zu schaffen.
    Bei einer Implementierung sollte darauf geachtet werden, dass sich "prioritaeten" nicht doppeln können.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Region.svg" type="image/svg+xml"></object>

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Region.json>`_

    """

    typ: Annotated[Literal[BoTyp.REGION], Field(alias="_typ")] = BoTyp.REGION
    bezeichnung: Optional[str] = None
    """Bezeichnung der Region"""
    beschreibung: Optional[str] = None
    """Beschreibung der Region"""

    regionsoperationen: Optional[list["Regionsoperation"]] = None
    """
    Eine (unsortierte) Liste von Regionsoperationen.
    Die Sortierung wird durch das Feld `prioritaet` im COM `Regionsoperation` festgelegt.
    """
