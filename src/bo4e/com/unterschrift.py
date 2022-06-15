"""
Contains Unterschrift class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Unterschrift(COM):
    """
    Modellierung einer Unterschrift, z.B. für Verträge, Angebote etc.

    .. HINT::
        `Unterschrift JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/UnterschriftSchema.json>`_

    """

    # required attributes
    #: Name des Unterschreibers
    name: str = attrs.field(validator=attrs.validators.instance_of(str))

    # optional attributes
    ort: str = attrs.field(default=None)  #: Ort, an dem die Unterschrift geleistet wird
    datum: datetime = attrs.field(default=None)  #: Datum der Unterschrift


class UnterschriftSchema(COMSchema):
    """
    Schema for de-/serialization of Unterschrift.
    """

    class_name = Unterschrift

    # required attributes
    name = fields.String()

    # optional attributes
    ort = fields.String(load_default=None)
    datum = fields.DateTime(load_default=None)
