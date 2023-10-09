"""
Contains Verwendungszweck class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.verwendungszweck import Verwendungszweck

# pylint: disable=too-few-public-methods


class Verwendungszweck(COM):
    """
    Verwendungungszweck der Werte Marktlokation

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verwendungszweck.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verwendungszweck JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Verwendungszweck.json>`_

    """

    marktrolle: Optional[Marktrolle] = None
    """
    Rollencodenummer der Marktrolle
    """
    Zwecke: Optional[list[Verwendungszweck]] = None
    """
    Verwendungszwecke
    """
