"""
Contains Region class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.regionskriterium import Regionskriterium, RegionskriteriumSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/RegionSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.REGION)
    #: Bezeichnung der Region
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))

    #: Positivliste der Kriterien zur Definition der Region
    positiv_liste: List[Regionskriterium] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Regionskriterium),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Negativliste der Kriterien zur Definition der Region
    negativ_liste: Optional[List[Regionskriterium]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Regionskriterium),
                iterable_validator=attrs.validators.instance_of(list),  # no min length for negativListe
            )
        ),
    )


class RegionSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Region
    """

    class_name = Region
    # required attributes
    bezeichnung = fields.Str()
    positiv_liste = fields.List(fields.Nested(RegionskriteriumSchema), data_key="positivListe")

    # optional attributes
    negativ_liste = fields.List(fields.Nested(RegionskriteriumSchema), load_default=None, data_key="negativListe")
