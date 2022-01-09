"""
Contains Region class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.regionskriterium import Regionskriterium, RegionskriteriumSchema
from bo4e.com.tagesvektor import Tagesvektor, TagesvektorSchema
from bo4e.com.zeitintervall import Zeitintervall, ZeitintervallSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.validators import obis_validator, check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.REGION)
    #: Bezeichnung der Region
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))

    #: Positivliste der Kriterien zur Definition der Region
    positiv_liste: List[Regionskriterium] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Regionskriterium),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Negativliste der Kriterien zur Definition der Region
    negativ_liste: Optional[List[Regionskriterium]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Regionskriterium),
                iterable_validator=attr.validators.instance_of(list),  # no min length for negativListe
            )
        ),
    )


class RegionSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Region
    """

    # required attributes
    bezeichnung = fields.Str()
    positiv_liste = fields.List(fields.Nested(RegionskriteriumSchema))

    # optional attributes
    negativ_liste = fields.List(fields.Nested(RegionskriteriumSchema), load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Region:
        """Deserialize JSON to Region object"""
        return Region(**data)