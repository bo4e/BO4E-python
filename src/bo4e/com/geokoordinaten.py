"""
Contains Geokoordinaten class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal


from marshmallow import fields

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class Geokoordinaten(COM):
    """
    This component provides the geo-coordinates for a location.

    .. HINT::
        `Geokoordinaten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/GeokoordinatenSchema.json>`_

    """

    breitengrad: Decimal
    laengengrad: Decimal
