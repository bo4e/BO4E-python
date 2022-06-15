"""
Contains Betrag class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.waehrungscode import Waehrungscode


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Betrag(COM):
    """
    Die Komponente wird dazu verwendet, Summenbeträge (beispielsweise in Angeboten und Rechnungen) als Geldbeträge
    abzubilden. Die Einheit ist dabei immer die Hauptwährung also Euro, Dollar etc…

    .. HINT::
        `Betrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/BetragSchema.json>`_

    """

    # required attributes
    wert: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))  #: Gibt den Betrag des Preises an.
    waehrung: Waehrungscode = attrs.field(
        validator=attrs.validators.instance_of(Waehrungscode)
    )  #: Die entsprechende Waehrung


class BetragSchema(COMSchema):
    """
    Schema for de-/serialization of Betrag
    """

    class_name = Betrag
    # required attributes
    wert = fields.Decimal(as_string=True)
    waehrung = EnumField(Waehrungscode)
