"""
Contains Zeitintervall class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField

from bo4e.com.com import COM, COMSchema
from bo4e.enum.zeiteinheit import Zeiteinheit


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zeitintervall(COM):
    """
    Abbildung für ein Zeitintervall. Die Abbildung eines Zeitintervalls.
    Z.B. zur Anwendung als Raster in äquidistanten Zeitreihen/Lastgängen, beispielsweise 15 Minuten.
    """

    # required attributes
    wert: int = attr.ib(validator=attr.validators.instance_of(int))
    zeiteinheit: Zeiteinheit = attr.ib(validator=attr.validators.instance_of(Zeiteinheit))


class ZeitintervallSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitintervall.
    """

    # required attributes
    wert = fields.Integer()
    vertragsteilende = EnumField(Zeiteinheit)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Zeitintervall:
        """Deserialize JSON to Vertragsteil object"""
        return Zeitintervall(**data)
