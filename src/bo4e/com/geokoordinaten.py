import attr

from decimal import Decimal
from marshmallow import Schema, fields, post_load

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class Geokoordinaten(COM):
    """
    This component provides the geo-coordinates for a location.
    """

    # = attr.ib() has to be there, to make the validator work
    breitengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    laengengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))


class GeokoordinatenSchema(Schema, JavaScriptMixin):
    """
    Standard json library can not serialise Decimal type.
    Therefore these information will be serialised as string.
    During the deserialisiation it will become a Decimal type again.
    Link to official documentain:
    https://marshmallow.readthedocs.io/en/latest/api_reference.html?highlight=function#marshmallow.fields.Decimal
    """

    breitengrad = fields.Decimal(as_string=True)
    laengengrad = fields.Decimal(as_string=True)

    @post_load
    def deserialise(self, data, **kwargs) -> Geokoordinaten:
        return Geokoordinaten(**data)
