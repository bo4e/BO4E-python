"""
Contains Zaehlzeitregister class and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..com.com import COM
from ..utils import postprocess_docstring

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
        `Zaehlzeitregister JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zaehlzeitregister.json>`_

    """

    zaehlzeit_definition: Optional[str] = None  #: Zählzeitdefinition
    zaehlzeit_register: Optional[str] = None  #: Zählzeitregister
    ist_schwachlastfaehig: Optional[bool] = None  #: Schwachlastfaehigkeit
