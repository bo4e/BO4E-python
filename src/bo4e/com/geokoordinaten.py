"""
Contains Geokoordinaten class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class Geokoordinaten(COM):
    """
    This component provides the geo-coordinates for a location.

    .. graphviz:: /api/dots/bo4e/com/Geokoordinaten.dot

    """

    breitengrad: Decimal
    laengengrad: Decimal
