"""
Contains ExterenzeReferenz class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class ExterneReferenz(COM):
    """
    Viele Datenobjekte weisen in unterschiedlichen Systemen eine eindeutige ID (Kundennummer, GP-Nummer etc.) auf.
    Beim Austausch von Datenobjekten zwischen verschiedenen Systemen ist es daher hilfreich,
    sich die eindeutigen IDs der anzubindenden Systeme zu merken.

    .. HINT::
        `ExterneReferenz JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ExterneReferenzSchema.json>`_

    """

    # required attributes
    ex_ref_name: str
    ex_ref_wert: str


class ExterneReferenzSchema(COMSchema):
    """
    Schema for de-/serialization of ExterneReferenz.
    Inherits from Schema and JavaScriptMixin.
    """

    class_name = ExterneReferenz
    ex_ref_name = fields.Str(data_key="exRefName")
    ex_ref_wert = fields.Str(data_key="exRefWert")
