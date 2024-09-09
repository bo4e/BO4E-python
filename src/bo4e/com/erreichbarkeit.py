"""
Contains Erreichbarkeit class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module

from typing import Optional

from ..com.zeitfenster import Zeitfenster
from ..utils import postprocess_docstring
from .com import COM


@postprocess_docstring
class Erreichbarkeit(COM):
    """
    Eine Komponente zur Abbildung der Erreichbarkeit

    .. raw:: html

        <object data="../_static/images/bo4e/com/Erreichbarkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `Erreichbarkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Erreichbarkeit.json>`_

    """

    montag_erreichbarkeit: Optional[Zeitfenster] = None

    dienstag_erreichbarkeit: Optional[Zeitfenster] = None

    mittwoch_erreichbarkeit: Optional[Zeitfenster] = None

    donnerstag_erreichbarkeit: Optional[Zeitfenster] = None

    freitag_erreichbarkeit: Optional[Zeitfenster] = None

    mittagspause: Optional[Zeitfenster] = None
