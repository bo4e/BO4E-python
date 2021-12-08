"""
Contains Unterschrift class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Unterschrift(COM):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.
    """

    # required attributes
    name: str = attr.ib(validator=attr.validators.instance_of(str))

    # optional attributes
    ort: str = attr.ib(default=None)
    datum: datetime = attr.ib(default=None)


class UnterschriftSchema(COMSchema):
    """
    Schema for de-/serialization of Unterschrift.
    """

    # required attributes
    name = fields.String()

    # optional attributes
    ort = fields.String(load_default=None)
    datum = fields.DateTime(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Unterschrift:
        """Deserialize JSON to Unterschrift object"""
        return Unterschrift(**data)
