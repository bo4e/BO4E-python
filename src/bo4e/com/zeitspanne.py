"""
contains the COM Zeitspanne
"""

from typing import Optional

import pydantic

from bo4e.com.com import COM

from ..utils import postprocess_docstring


@postprocess_docstring
class Zeitspanne(COM):
    """
    Eine Zeitspanne ist definiert aus Start und/oder Ende.
    Der Unterschied zur Menge (die auch zur Abbildung von Zeitmengen genutzt wird) ist, dass konkrete Start- und Endzeitpunkte angegeben werden.
    Die Zeitspanne ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Menge aufgeteilt wurde.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitspanne.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitspanne JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zeitspanne.json>`_

    """

    start: Optional[pydantic.AwareDatetime] = None  #: inklusiver Beginn
    ende: Optional[pydantic.AwareDatetime] = None  #: exklusives Ende
