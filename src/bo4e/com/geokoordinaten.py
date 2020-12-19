import attr

from decimal import Decimal
from marshmallow import Schema, fields, post_load

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class Geokoordinaten(COM):
    """
    Diese Komponente liefert die Geokoordinaten für einen Ort.
    """

    # = attr.ib() has to be there, to make the validator work
    breitengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    laengengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))


class GeokoordinatenSchema(Schema, JavaScriptMixin):
    # standard json library can not serialise Decimal type
    # therefor these information will be serialised as string
    # during the deserialisiation it will become a Decimal type again
    breitengrad = fields.Decimal(as_string=True)
    laengengrad = fields.Decimal(as_string=True)

    @post_load
    def make_geokoordinaten(self, data, **kwargs) -> Geokoordinaten:
        return Geokoordinaten(**data)
