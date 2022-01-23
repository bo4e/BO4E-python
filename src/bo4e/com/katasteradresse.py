"""
Contains Katasteradresse class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Katasteradresse(COM):
    """
    Dient der Adressierung über die Liegenschafts-Information.
    """

    gemarkung_flur: str
    flurstueck: str


class KatasteradresseSchema(COMSchema):
    """
    Schema for de-/serialization of Katasteradresse.
    """

    class_name = Katasteradresse
    gemarkung_flur = fields.Str()
    flurstueck = fields.Str()
