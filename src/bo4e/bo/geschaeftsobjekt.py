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
    base class for all business objects
    """

    versionstruktur: int = attr.ib(default=2)
    bo_typ: BoTyp
    externe_referenzen: Optional[List[ExterneReferenz]] = attr.ib(
        default=None, validator=attr.validators.instance_of((type(None), List))
    )


class GeschaeftsobjektSchema(Schema, JavaScriptMixin):
    class_name = Geschaeftsobjekt

    versionstruktur = fields.Integer()
    bo_typ = EnumField(BoTyp)
    externe_referenzen = fields.List(fields.Nested(ExterneReferenzSchema), missing=None)

    @post_load
    def deserialise(self, data, **kwargs):
        return type(self).class_name(**data)
