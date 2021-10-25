"""
Contains Dienstleistung class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Dienstleistung(COM):
    """
    Abbildung einer abrechenbaren Dienstleistung.
    """

    # required attributes
    dienstleistungstyp: Dienstleistungstyp = attr.ib(validator=attr.validators.in_(Dienstleistungstyp))
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))


class DienstleistungSchema(COMSchema):
    """
    Schema for de-/serialization of Dienstleistung.
    """

    # required attributes
    dienstleistungstyp = EnumField(Dienstleistungstyp)
    bezeichnung = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Dienstleistung:
        """Deserialize JSON to Dienstleistung object"""
        return Dienstleistung(**data)
