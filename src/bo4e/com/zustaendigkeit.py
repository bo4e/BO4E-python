"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField
from bo4e.com.com import COM, COMSchema
from bo4e.enum.rufnummernart import Rufnummernart
from bo4e.enum.themengebiet import Themengebiet


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
    jobtitel: str = fields.Str(missing=None)
    abteilung: str = fields.Str(missing=None)

    # pylint: disable=no-self-use
    @post_load
    def deserialize(self, data, **kwargs) -> Zustaendigkeit:
        """Deserialize JSON to Zustaendigkeit object"""
        return Zustaendigkeit(**data)
