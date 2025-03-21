"""
Contains Zaehlzeitregister class
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=no-name-in-module
# pylint: disable=too-few-public-methods


@postprocess_docstring
class Zaehlzeitregister(COM):
    """
    Mit dieser Komponente werden Zählzeitregister modelliert. Ein Zählzeitregister beschreibt eine erweiterte Definition der Zählzeit
    in Bezug auf ein Register. Dabei werden alle Codes dazu vom Netzbetreiber vergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlzeitregister.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitregister JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zaehlzeitregister.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZAEHLZEITREGISTER], Field(alias="_typ")] = ComTyp.ZAEHLZEITREGISTER

    zaehlzeit_definition: Optional[str] = None
    """Zählzeitdefinition"""
    zaehlzeit_register: Optional[str] = None
    """Zählzeitregister"""
    ist_schwachlastfaehig: Optional[bool] = None
    """Schwachlastfaehigkeit"""
