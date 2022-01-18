"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

import attr
from marshmallow import fields

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.vertrag import Vertrag, VertragSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Buendelvertrag(Geschaeftsobjekt):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.BUENDELVERTRAG)
    #: Die Liste mit den Einzelverträgen zu den Abnahmestellen
    einzelvertraege: List[Vertrag] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Vertrag), iterable_validator=check_list_length_at_least_one
        )
    )


class BuendelvertragSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Buendelvertrag
    """

    class_name = Buendelvertrag

    # required attributes
    einzelvertraege = fields.List(fields.Nested(VertragSchema))
