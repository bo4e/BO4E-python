"""
Contains Rufnummer class and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.rufnummernart import Rufnummernart


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Rufnummer(COM):
    """
    Contains information to call or fax someone

    .. HINT::
        `Rufnummer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RufnummerSchema.json>`_

    """

    # required attributes
    nummerntyp: Rufnummernart = attr.ib(validator=attr.validators.in_(Rufnummernart))
    rufnummer: str = attr.ib(validator=attr.validators.instance_of(str))


class RufnummerSchema(COMSchema):
    """
    Schema for de-/serialization of Rufnummer.
    """

    class_name = Rufnummer
    # required attributes
    nummerntyp = EnumField(Rufnummernart)
    rufnummer = fields.Str()
