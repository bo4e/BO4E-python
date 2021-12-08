"""
Contains KriteriumWert class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema

# pylint: disable=too-few-public-methods
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium


@attr.s(auto_attribs=True, kw_only=True)
class KriteriumWert(COM):
    """
    Mit dieser Komponente können Kriterien und deren Werte definiert werden
    """

    # required attributes
    #: Hier steht, für welches Kriterium der Wert gilt. Z.B. Postleitzahlen
    kriterium: Tarifregionskriterium = attr.ib(validator=attr.validators.instance_of(Tarifregionskriterium))
    #: Ein Wert, passend zum Kriterium. Z.B. eine Postleitzahl.
    wert: str = attr.ib(validator=attr.validators.instance_of(str))


class KriteriumWertSchema(COMSchema):
    """
    Schema for de-/serialization of KriteriumWert.
    """

    # required attributes
    kriterium = EnumField(Tarifregionskriterium)
    wert = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> KriteriumWert:
        """Deserialize JSON to KriteriumWert object"""
        return KriteriumWert(**data)
