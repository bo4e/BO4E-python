"""
Contains base class for all business objects
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=unused-argument, too-few-public-methods
from typing import List, Optional, Type

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.externereferenz import ExterneReferenz, ExterneReferenzSchema
from bo4e.enum.botyp import BoTyp
from bo4e.schemata.caseconverterschema import CaseConverterSchema


def _create_empty_referenzen_list() -> List[ExterneReferenz]:
    """
    A method with a type hint to please mypy
    https://stackoverflow.com/a/61281305/10009545
    :return:
    """
    return []


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftsobjekt:
    """
    Base class for all business objects
    """

    # required attributes
    versionstruktur: str = attr.ib(default="2")
    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSOBJEKT)

    # optional attributes
    externe_referenzen: Optional[List[ExterneReferenz]] = attr.ib(
        default=_create_empty_referenzen_list(), validator=attr.validators.instance_of(List)  # type:ignore[arg-type]
    )


class GeschaeftsobjektSchema(CaseConverterSchema):
    """
    This is an "abstract" class.
    All business objects schemata do inherit from this class.
    """

    # class_name is needed to use the correct schema for deserialization.
    class_name: Type[Geschaeftsobjekt] = Geschaeftsobjekt

    # required attributes
    versionstruktur = fields.String()
    bo_typ = EnumField(BoTyp)

    # optional attributes
    externe_referenzen = fields.List(fields.Nested(ExterneReferenzSchema), load_default=None)

    @post_load
    def deserialize(self, data, **kwargs):
        """Deserialize JSON to python object."""
        return type(self).class_name(**data)
