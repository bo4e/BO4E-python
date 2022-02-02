"""
Contains Zustaendigkeit class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.themengebiet import Themengebiet


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZustaendigkeitSchema.json>`_

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

    class_name = Zustaendigkeit
    # required attributes
    themengebiet = EnumField(Themengebiet)

    # optional attributes
    jobtitel = fields.Str(load_default=None)
    abteilung = fields.Str(load_default=None)
