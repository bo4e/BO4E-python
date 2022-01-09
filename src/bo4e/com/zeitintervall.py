"""
Contains Zeitintervall class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.zeiteinheit import Zeiteinheit


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zeitintervall(COM):
    """
    Abbildung für ein Zeitintervall. Die Abbildung eines Zeitintervalls.
    Z.B. zur Anwendung als Raster in äquidistanten Zeitreihen/Lastgängen, beispielsweise 15 Minuten.
    """

    # required attributes
    wert: int = attr.ib(validator=attr.validators.instance_of(int))
    zeiteinheit: Zeiteinheit = attr.ib(validator=attr.validators.instance_of(Zeiteinheit))


class ZeitintervallSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitintervall.
    """

    class_name = Zeitintervall
    # required attributes
    wert = fields.Integer()
    zeiteinheit = EnumField(Zeiteinheit)
