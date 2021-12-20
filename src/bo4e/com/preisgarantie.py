"""
Contains Preisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.preisgarantietyp import Preisgarantietyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Preisgarantie(COM):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.
    """

    # required attributes
    #: Festlegung, auf welche Preisbestandteile die Garantie gewährt wird.
    preisgarantietyp: Preisgarantietyp = attr.ib(validator=attr.validators.instance_of(Preisgarantietyp))
    zeitliche_gueltigkeit: Zeitraum = attr.ib(validator=attr.validators.instance_of(Zeitraum))
    """ Zeitraum, bis zu dem die Preisgarantie gilt, z.B. bis zu einem absolutem / fixem Datum
    oder als Laufzeit in Monaten. """

    # optionale attributes
    #: Freitext zur Beschreibung der Preisgarantie.
    beschreibung: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )


class PreisgarantieSchema(COMSchema):
    """
    Schema for de-/serialization of Preisgarantie.
    """

    # required attributes
    preisgarantietyp = EnumField(Preisgarantietyp)
    zeitliche_gueltigkeit = fields.Nested(ZeitraumSchema)

    # optionale attributes
    beschreibung = fields.Str(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Preisgarantie:
        """Deserialize JSON to Preisgarantie object"""
        return Preisgarantie(**data)
