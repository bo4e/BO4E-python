"""
Contains Betrag class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema

# pylint: disable=too-few-public-methods
from bo4e.enum.waehrungscode import Waehrungscode


@attr.s(auto_attribs=True, kw_only=True)
class Betrag(COM):
    """
    Die Komponente wird dazu verwendet, Summenbeträge (beispielsweise in Angeboten und Rechnungen) als Geldbeträge
    abzubilden. Die Einheit ist dabei immer die Hauptwährung also Euro, Dollar etc…
    """

    # required attributes
    wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Gibt den Betrag des Preises an.
    waehrung: Waehrungscode = attr.ib(
        validator=attr.validators.instance_of(Waehrungscode)
    )  #: Die entsprechende Waehrung


class BetragSchema(COMSchema):
    """
    Schema for de-/serialization of Betrag.
    """

    # required attributes
    wert = fields.Decimal(as_string=True)
    waehrung = EnumField(Waehrungscode)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Betrag:
        """Deserialize JSON to Betrag object"""
        return Betrag(**data)
