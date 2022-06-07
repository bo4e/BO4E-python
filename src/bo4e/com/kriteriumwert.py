"""
Contains KriteriumWert class
and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema

# pylint: disable=too-few-public-methods
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium


@attrs.define(auto_attribs=True, kw_only=True)
class KriteriumWert(COM):
    """
    Mit dieser Komponente können Kriterien und deren Werte definiert werden

    .. HINT::
        `KriteriumWert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/KriteriumWertSchema.json>`_

    """

    # required attributes
    #: Hier steht, für welches Kriterium der Wert gilt. Z.B. Postleitzahlen
    kriterium: Tarifregionskriterium = attrs.field(validator=attrs.validators.instance_of(Tarifregionskriterium))
    #: Ein Wert, passend zum Kriterium. Z.B. eine Postleitzahl.
    wert: str = attrs.field(validator=attrs.validators.instance_of(str))


class KriteriumWertSchema(COMSchema):
    """
    Schema for de-/serialization of KriteriumWert.
    """

    class_name = KriteriumWert
    # required attributes
    kriterium = EnumField(Tarifregionskriterium)
    wert = fields.Str()
