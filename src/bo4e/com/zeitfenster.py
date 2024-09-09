"""
Contains Zeitfenster class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module

from datetime import time
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM


@postprocess_docstring
class Zeitfenster(COM):
    """
    Eine Komponente zur Abbildung des Zeitfensters für die Erreichbarkeit

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitfenster.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitfenster JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zeitfenster.json>`_

    """

    startzeit: Optional[time] = None
    endzeit: Optional[time] = None
