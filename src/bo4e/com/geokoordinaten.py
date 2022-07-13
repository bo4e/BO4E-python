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

    .. raw:: html

        <object data="../_static/images/bo4e/com/Geokoordinaten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geokoordinaten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Geokoordinaten.json>`_

    """

    breitengrad: Decimal
    laengengrad: Decimal
