"""
Contains Menge class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

from decimal import Decimal

from bo4e.com.com import COM
from bo4e.enum.mengeneinheit import Mengeneinheit


# pylint: disable=too-few-public-methods


class Menge(COM):
    """
    Abbildung einer Menge mit Wert und Einheit.

    .. HINT::
        `Menge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/MengeSchema.json>`_

    """

    # required attributes
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal
    #: Gibt die Einheit zum jeweiligen Wert an
    einheit: Mengeneinheit
