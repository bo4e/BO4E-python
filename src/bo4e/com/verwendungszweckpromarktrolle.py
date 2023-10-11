"""
Contains Verwendungszweck class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..com.com import COM
from ..enum.marktrolle import Marktrolle
from ..enum.verwendungszweck import Verwendungszweck

# pylint: disable=too-few-public-methods


class VerwendungszweckProMarktrolle(COM):
    """
    Dient zur Identifizierung des Verwendungszwecks der Marktrolle an der Marktlokation, der die Werte zu übermitteln sind.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verwendungszweck.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verwendungszweck JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Verwendungszweck.json>`_

    """

    marktrolle: Optional[Marktrolle] = None
    """
    Marktrolle, für die die Daten relevant sind
    """
    Zwecke: Optional[list[Verwendungszweck]] = None
    """
    Verwendungszwecke
    """
