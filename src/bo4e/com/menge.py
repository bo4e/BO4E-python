"""
Contains Menge class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from ..enum.mengeneinheit import Mengeneinheit
from .com import COM

# pylint: disable=too-few-public-methods


class Menge(COM):
    """
    Abbildung einer Menge mit Wert und Einheit.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Menge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Menge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Menge.json>`_

    """

    #: Gibt den absoluten Wert der Menge an
    wert: Optional[Decimal] = None
    #: Gibt die Einheit zum jeweiligen Wert an
    einheit: Optional[Mengeneinheit] = None
