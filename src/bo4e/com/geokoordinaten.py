"""
Contains Geokoordinaten class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Geokoordinaten(COM):
    """
    This component provides the geo-coordinates for a location.
    """

    # = attr.ib() has to be there, to make the validator work
    breitengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    laengengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))


class GeokoordinatenSchema(COMSchema):
    """
    Schema for de-/serialization of Geokoordinaten.

    Standard json library can not serialize Decimal type.
    Therefore these information will be serialized as string.
    During the deserialisiation it will become a Decimal type again.
    Link to official documentain:
    https://marshmallow.readthedocs.io/en/latest/api_reference.html?highlight=function#marshmallow.fields.Decimal
    """

    breitengrad = fields.Decimal(as_string=True)
    laengengrad = fields.Decimal(as_string=True)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Geokoordinaten:
        """Deserialize JSON to Geokoordinaten object"""
        return Geokoordinaten(**data)
