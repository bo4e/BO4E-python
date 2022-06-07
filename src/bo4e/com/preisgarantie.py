"""
Contains Preisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.preisgarantietyp import Preisgarantietyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Preisgarantie(COM):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.

    .. HINT::
        `Preisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PreisgarantieSchema.json>`_

    """

    # required attributes
    #: Festlegung, auf welche Preisbestandteile die Garantie gewährt wird.
    preisgarantietyp: Preisgarantietyp = attrs.field(validator=attrs.validators.instance_of(Preisgarantietyp))
    zeitliche_gueltigkeit: Zeitraum = attrs.field(validator=attrs.validators.instance_of(Zeitraum))
    """ Zeitraum, bis zu dem die Preisgarantie gilt, z.B. bis zu einem absolutem / fixem Datum
    oder als Laufzeit in Monaten. """

    # optionale attributes
    #: Freitext zur Beschreibung der Preisgarantie.
    beschreibung: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )


class PreisgarantieSchema(COMSchema):
    """
    Schema for de-/serialization of Preisgarantie.
    """

    class_name = Preisgarantie
    # required attributes
    preisgarantietyp = EnumField(Preisgarantietyp)
    zeitliche_gueltigkeit = fields.Nested(ZeitraumSchema, data_key="zeitlicheGueltigkeit")

    # optionale attributes
    beschreibung = fields.Str(load_default=None)
