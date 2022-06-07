"""
Contains Dienstleistung class
and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Dienstleistung(COM):
    """
    Abbildung einer abrechenbaren Dienstleistung.

    .. HINT::
        `Dienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/DienstleistungSchema.json>`_

    """

    # required attributes
    #: Kennzeichnung der Dienstleistung
    dienstleistungstyp: Dienstleistungstyp = attrs.field(validator=attrs.validators.in_(Dienstleistungstyp))
    #: Bezeichnung der Dienstleistung
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))


class DienstleistungSchema(COMSchema):
    """
    Schema for de-/serialization of Dienstleistung.
    """

    class_name = Dienstleistung
    # required attributes
    dienstleistungstyp = EnumField(Dienstleistungstyp)
    bezeichnung = fields.Str()
