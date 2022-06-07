"""
Contains Geokoordinaten class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Geokoordinaten(COM):
    """
    This component provides the geo-coordinates for a location.

    .. HINT::
        `Geokoordinaten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/GeokoordinatenSchema.json>`_

    """

    # = attrs.field() has to be there, to make the validator work
    breitengrad: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    laengengrad: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))


class GeokoordinatenSchema(COMSchema):
    """
    Schema for de-/serialization of Geokoordinaten.

    Standard json library can not serialize Decimal type.
    Therefore these information will be serialized as string.
    During the deserialisiation it will become a Decimal type again.
    Link to official documentain:
    https://marshmallow.readthedocs.io/en/latest/api_reference.html?highlight=function#marshmallow.fields.Decimal
    """

    class_name = Geokoordinaten

    breitengrad = fields.Decimal(as_string=True)
    laengengrad = fields.Decimal(as_string=True)
