"""
Contains Preis class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Preis(COM):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PreisSchema.json>`_

    """

    # required attributes
    #: Gibt die nominale Höhe des Preises an.
    wert: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Währungseinheit für den Preis, z.B. Euro oder Ct.
    einheit: Waehrungseinheit = attrs.field(validator=attrs.validators.in_(Waehrungseinheit))
    #: Angabe, für welche Bezugsgröße der Preis gilt. Z.B. kWh.
    bezugswert: Mengeneinheit = attrs.field(validator=attrs.validators.in_(Mengeneinheit))

    # optional attributes
    #: Gibt den Status des veröffentlichten Preises an
    status: Optional[Preisstatus] = attrs.field(default=None)


class PreisSchema(COMSchema):
    """
    Schema for de-/serialization of Preis.
    """

    class_name = Preis
    # required attributes
    wert = fields.Decimal(as_string=True)
    einheit = EnumField(Waehrungseinheit)
    bezugswert = EnumField(Mengeneinheit)

    # optional attributes
    status = EnumField(Preisstatus, load_default=None)
