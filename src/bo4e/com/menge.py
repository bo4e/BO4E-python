"""
Contains Menge class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

from bo4e.com.com import COM
from bo4e.enum.mengeneinheit import Mengeneinheit


# pylint: disable=too-few-public-methods


class Menge(COM):
    """
    Abbildung einer Menge mit Wert und Einheit.

    .. graphviz:: /api/dots/bo4e/com/Menge.dot

    """

    # required attributes
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal
    #: Gibt die Einheit zum jeweiligen Wert an
    einheit: Mengeneinheit
