"""
Contains Unterschrift class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

from .com import COM

# pylint: disable=too-few-public-methods


class Unterschrift(COM):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Unterschrift.svg" type="image/svg+xml"></object>

    .. HINT::
        `Unterschrift JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Unterschrift.json>`_

    """

    #: Name des Unterschreibers
    name: Optional[str] = None

    ort: Optional[str] = None  #: Ort, an dem die Unterschrift geleistet wird
    datum: Optional[datetime] = None  #: Datum der Unterschrift
