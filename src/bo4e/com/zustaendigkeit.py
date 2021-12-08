"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.themengebiet import Themengebiet


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.
    """

    # required attributes
    themengebiet: Themengebiet = attr.ib(validator=attr.validators.in_(Themengebiet))

    # optional attributes
    jobtitel: str = attr.ib(default=None)
    abteilung: str = attr.ib(default=None)


class ZustaendigkeitSchema(COMSchema):
    """
    Schema for de-/serialization of Zustaendigkeit.
    """

    # required attributes
    themengebiet = EnumField(Themengebiet)

    # optional attributes
    jobtitel = fields.Str(load_default=None)
    abteilung = fields.Str(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Zustaendigkeit:
        """Deserialize JSON to Zustaendigkeit object"""
        return Zustaendigkeit(**data)
