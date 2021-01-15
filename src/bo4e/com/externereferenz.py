import attr
from marshmallow import Schema, fields, post_load

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM


@attr.s(auto_attribs=True, kw_only=True)
class ExterneReferenz(COM):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf. Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich, sich die eindeutigen IDs der anzubindenden Systeme zu merken.
    """

    # required attributes
    ex_ref_name: str
    ex_ref_wert: str


class ExterneReferenzSchema(Schema, JavaScriptMixin):
    ex_ref_name = fields.Str()
    ex_ref_wert = fields.Str()

    @post_load
    def deserialise(self, data, **kwargs) -> ExterneReferenz:
        return ExterneReferenz(**data)
