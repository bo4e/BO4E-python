"""
Contains Hardware class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Hardware(COM):
    """
    Abbildung einer abrechenbaren Hardware.
    """

    # required attributes
    geraetetyp: Geraetetyp = attr.ib(validator=attr.validators.in_(Geraetetyp))
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))


class HardwareSchema(COMSchema):
    """
    Schema for de-/serialization of Hardware.
    """

    # required attributes
    geraetetyp = EnumField(Geraetetyp)
    bezeichnung = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Hardware:
        """Deserialize JSON to Hardware object"""
        return Hardware(**data)
