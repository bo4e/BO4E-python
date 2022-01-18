"""
Contains Energiemenge class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.verbrauch import Verbrauch, VerbrauchSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Energiemenge(Geschaeftsobjekt):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.ENERGIEMENGE)
    #: Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört
    lokations_id: str = attr.ib(validator=attr.validators.instance_of(str))
    # todo: add validator such that only mess- or marktlokations IDs are accepted + cross check with lokationstyp
    #: Gibt an, ob es sich um eine Markt- oder Messlokation handelt
    lokationstyp: Lokationstyp = attr.ib(validator=attr.validators.instance_of(Lokationstyp))

    #: Gibt den Verbrauch in einer Zeiteinheit an
    energieverbrauch: List[Verbrauch] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Verbrauch),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # there are no optional attributes


class EnergiemengeSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Energiemenge
    """

    class_name = Energiemenge
    # required attributes
    lokations_id = fields.Str()
    lokationstyp = EnumField(Lokationstyp)
    energieverbrauch = fields.List(fields.Nested(VerbrauchSchema))
