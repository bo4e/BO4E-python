"""
Contains Geraet class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften, GeraeteeigenschaftenSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Geraet(COM):
    """
    Mit dieser Komponente werden alle Geräte modelliert, die keine Zähler sind.

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/GeraetSchema.json>`_

    """

    # optional attributes
    #: Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    geraetenummer: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS.
    geraeteeigenschaften: Optional[Geraeteeigenschaften] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Geraeteeigenschaften))
    )


class GeraetSchema(COMSchema):
    """
    Schema for de-/serialization of Geraet.
    """

    class_name = Geraet
    # optional attributes
    geraetenummer = fields.Str(load_default=None)
    geraeteeigenschaften = fields.Nested(GeraeteeigenschaftenSchema, missing=None)
