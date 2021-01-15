from typing import List, Optional

import attr
from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField
from bo4e.cases import JavaScriptMixin

from bo4e.com.externereferenz import ExterneReferenz, ExterneReferenzSchema
from bo4e.enum.botyp import BoTyp


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftsobjekt:
    """
    Base class for all business objects
    """

    # required attributes
    versionstruktur: int = attr.ib(default=2)
    bo_typ: BoTyp

    # optional attributes
    externe_referenzen: Optional[List[ExterneReferenz]] = attr.ib(
        default=None, validator=attr.validators.instance_of((type(None), List))
    )


class GeschaeftsobjektSchema(Schema, JavaScriptMixin):
    """
    This is an "abstract" class.
    All business objects are inherited from this class.
    """

    # class_name is needed to use the correct schema for deserialization.
    class_name = Geschaeftsobjekt

    # required attributes
    versionstruktur = fields.Integer()
    bo_typ = EnumField(BoTyp)

    # optional attributes
    externe_referenzen = fields.List(fields.Nested(ExterneReferenzSchema), missing=None)

    @post_load
    def deserialise(self, data, **kwargs):
        return type(self).class_name(**data)
