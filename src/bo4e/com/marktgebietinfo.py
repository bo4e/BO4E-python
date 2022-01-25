"""
Contains Marktgebietinfo class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class MarktgebietInfo(COM):
    """
    Informationen zum Marktgebiet im Gas.

    .. HINT::
        `MarktgebietInfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/com/MarktgebietInfoSchema.json>`_

    """

    # required attributes
    marktgebiet: str  #: Der Name des Marktgebietes
    marktgebietcode: str  #: Die standardisierte Codenummer des Marktgebietes


class MarktgebietInfoSchema(COMSchema):
    """
    Schema for de-/serialization of Marktgebietinfo.
    """

    class_name = MarktgebietInfo
    # required attributes
    marktgebiet = fields.Str()
    marktgebietcode = fields.Str()
