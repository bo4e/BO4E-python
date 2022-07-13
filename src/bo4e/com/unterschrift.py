"""
Contains Unterschrift class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

from bo4e.com.com import COM

# pylint: disable=too-few-public-methods


class Unterschrift(COM):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Unterschrift.svg" type="image/svg+xml"></object>

    .. HINT::
        `Unterschrift JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Unterschrift.json>`_

    """

    # required attributes
    #: Name des Unterschreibers
    name: str

    # optional attributes
    ort: Optional[str] = None  #: Ort, an dem die Unterschrift geleistet wird
    datum: Optional[datetime] = None  #: Datum der Unterschrift
