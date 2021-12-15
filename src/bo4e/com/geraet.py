"""
Contains Geraet class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften, GeraeteeigenschaftenSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Geraet(COM):
    """
    Mit dieser Komponente werden alle Geräte modelliert, die keine Zähler sind.
    """

    # optional attributes
    #: Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    geraetenummer: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    #: Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS.
    geraeteeigenschaften: Optional[Geraeteeigenschaften] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Geraeteeigenschaften))
    )


class GeraetSchema(COMSchema):
    """
    Schema for de-/serialization of Geraet.
    """

    # optional attributes
    geraetenummer = fields.Str(missing=None)
    geraeteeigenschaften = fields.Nested(GeraeteeigenschaftenSchema, missing=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Geraet:
        """Deserialize JSON to Geraet object"""
        return Geraet(**data)
