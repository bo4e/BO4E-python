import attr

from marshmallow import Schema, fields, post_load

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class Katasteradresse(COM):
    """
    Dient der Adressierung über die Liegenschafts-Information.
    """

    gemarkung_flur: str
    flurstueck: str


class KatasteradresseSchema(Schema, JavaScriptMixin):
    gemarkung_flur = fields.Str()
    flurstueck = fields.Str()

    @post_load
    def deserialise(self, data, **kwargs) -> Katasteradresse:
        return Katasteradresse(**data)
