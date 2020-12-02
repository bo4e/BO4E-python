from decimal import Decimal
import attr
import jsons

from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class Geokoordinaten(COM, jsons.JsonSerializable):
    """
    Diese Komponente liefert die Geokoordinaten für einen Ort.
    """

    # = attr.ib() has to be there, to make the validator work
    breitengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    laengengrad: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
