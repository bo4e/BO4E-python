"""
Contains ExterenzeReferenz class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class ExterneReferenz(COM):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf.
    Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich,
    sich die eindeutigen IDs der anzubindenden Systeme zu merken.
    """

    # required attributes
    ex_ref_name: str
    ex_ref_wert: str


class ExterneReferenzSchema(COMSchema):
    """
    Schema for de-/serialization of ExterneReferenz.
    Inherits from Schema and JavaScriptMixin.
    """

    ex_ref_name = fields.Str()
    ex_ref_wert = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> ExterneReferenz:
        """Deserialize JSON to ExterneReferenz object"""
        return ExterneReferenz(**data)
