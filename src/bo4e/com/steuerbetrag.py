"""
Contains Steuerbetrag class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.steuerkennzeichen import Steuerkennzeichen
from bo4e.enum.waehrungscode import Waehrungscode


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Steuerbetrag(COM):
    """
    Abbildung eines Steuerbetrages.
    """

    # required attributes
    #: Kennzeichnung des Steuersatzes, bzw. Verfahrens.
    steuerkennzeichen: Steuerkennzeichen = attr.ib(validator=attr.validators.in_(Steuerkennzeichen))
    #: Nettobetrag für den die Steuer berechnet wurde. Z.B. 100
    basiswert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Aus dem Basiswert berechnete Steuer. Z.B. 19 (bei UST_19)
    steuerwert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Währung. Z.B. Euro.
    waehrung: Waehrungscode = attr.ib(validator=attr.validators.in_(Waehrungscode))


class SteuerbetragSchema(COMSchema):
    """
    Schema for de-/serialization of Steuerbetrag.
    """

    # required attributes
    steuerkennzeichen = EnumField(Steuerkennzeichen)
    basiswert = fields.Decimal(as_string=True)
    steuerwert = fields.Decimal(as_string=True)
    waehrung = EnumField(Waehrungscode)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Steuerbetrag:
        """Deserialize JSON to Steuerbetrag object"""
        return Steuerbetrag(**data)
