"""
Contains Menge class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.mengeneinheit import Mengeneinheit


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Menge(COM):
    """
    Abbildung einer Menge mit Wert und Einheit.
    """

    # required attributes
    wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    einheit: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))


class MengeSchema(COMSchema):
    """
    Schema for de-/serialization of Menge.
    """

    # required attributes
    wert = fields.Decimal(as_string=True)
    einheit = EnumField(Mengeneinheit)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Menge:
        """Deserialize JSON to Menge object"""
        return Menge(**data)
