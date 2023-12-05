"""
Contains Geokoordinaten class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Geokoordinaten(COM):
    """
    This component provides the geo-coordinates for a location.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Geokoordinaten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geokoordinaten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Geokoordinaten.json>`_

    """

    breitengrad: Optional[Decimal] = None
    laengengrad: Optional[Decimal] = None
