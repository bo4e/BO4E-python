"""
Contains TarifpreispositionProOrt class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .tarifpreisstaffelproort import TarifpreisstaffelProOrt

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class TarifpreispositionProOrt(COM):
    """
    Mit dieser Komponente können Tarifpreise verschiedener Typen abgebildet werden

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifpreispositionProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifpreispositionProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/TarifpreispositionProOrt.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIFPREISPOSITIONPROORT], Field(alias="_typ")] = ComTyp.TARIFPREISPOSITIONPROORT

    postleitzahl: Optional[str] = None
    """Postleitzahl des Ortes für den der Preis gilt"""
    ort: Optional[str] = None
    """Ort für den der Preis gilt"""
    netznr: Optional[str] = None
    """ene't-Netznummer des Netzes in dem der Preis gilt"""
    # Hier sind die Staffeln mit ihren Preisenangaben definiert
    preisstaffeln: Optional[list["TarifpreisstaffelProOrt"]] = None
    # there are no optional attributes
