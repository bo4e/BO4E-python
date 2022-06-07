"""
Contains Katasteradresse class
and corresponding marshmallow schema for de-/serialization
"""
import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Katasteradresse(COM):
    """
    Dient der Adressierung über die Liegenschafts-Information.

    .. HINT::
        `Katasteradresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/KatasteradresseSchema.json>`_

    """

    gemarkung_flur: str
    flurstueck: str


class KatasteradresseSchema(COMSchema):
    """
    Schema for de-/serialization of Katasteradresse.
    """

    class_name = Katasteradresse
    gemarkung_flur = fields.Str(data_key="gemarkungFlur")
    flurstueck = fields.Str()
