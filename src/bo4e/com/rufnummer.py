"""
Contains Rufnummer class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField
from bo4e.com.com import COM, COMSchema
from bo4e.enum.rufnummernart import Rufnummernart


@attr.s(auto_attribs=True, kw_only=True)
class Rufnummer(COM):
    """
    Contains information to call or fax someone
    """

    # required attributes
    nummerntyp: Rufnummernart = attr.ib(validator=attr.validators.in_(Rufnummernart))
    rufnummer: str = attr.ib(validator=attr.validators.instance_of(str))


class RufnummerSchema(COMSchema):
    """
    Schema for de-/serialization of Rufnummer.
    """

    # required attributes
    nummerntyp = EnumField(Rufnummernart)
    rufnummer = fields.Str()

    # pylint: disable=no-self-use
    @post_load
    def deserialize(self, data, **kwargs) -> Rufnummer:
        """Deserialize JSON to Rufnummer object"""
        return Rufnummer(**data)
