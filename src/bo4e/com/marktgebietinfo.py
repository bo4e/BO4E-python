"""
Contains Marktgebietinfo class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Marktgebietinfo(COM):
    """
    Informationen zum Marktgebiet im Gas.
    """

    marktgebiet: str
    marktgebietcode: str


class MarktgebietinfoSchema(COMSchema):
    """
    Schema for de-/serialization of Marktgebietinfo.
    """

    marktgebiet = fields.Str()
    marktgebietcode = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Marktgebietinfo:
        """Deserialize JSON to Marktgebietinfo object"""
        return Marktgebietinfo(**data)
