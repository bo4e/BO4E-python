"""
Contains Hardware class
and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Hardware(COM):
    """
    Abbildung einer abrechenbaren Hardware

    .. HINT::
        `Hardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/HardwareSchema.json>`_

    """

    # required attributes
    #: Eindeutiger Typ der Hardware
    geraetetyp: Geraetetyp = attrs.field(validator=attrs.validators.in_(Geraetetyp))
    #: Bezeichnung der Hardware
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))


class HardwareSchema(COMSchema):
    """
    Schema for de-/serialization of Hardware.
    """

    class_name = Hardware
    # required attributes
    geraetetyp = EnumField(Geraetetyp)
    bezeichnung = fields.Str()
