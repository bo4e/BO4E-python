"""
Contains Preis class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Preis(COM):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.
    """

    # required attributes
    wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    einheit: Waehrungseinheit = attr.ib(validator=attr.validators.in_(Waehrungseinheit))
    bezugswert: Mengeneinheit = attr.ib(validator=attr.validators.in_(Mengeneinheit))

    # optional attributes
    status: Optional[Preisstatus] = attr.ib(default=None)


class PreisSchema(COMSchema):
    """
    Schema for de-/serialization of Preis.
    """

    # required attributes
    wert = fields.Decimal(as_string=True)
    einheit = EnumField(Waehrungseinheit)
    bezugswert = EnumField(Mengeneinheit)

    # optional attributes
    status = EnumField(Preisstatus, load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Preis:
        """Deserialize JSON to Preis object"""
        return Preis(**data)
