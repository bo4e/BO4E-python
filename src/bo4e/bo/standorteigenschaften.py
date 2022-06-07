"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein, StandorteigenschaftenAllgemeinSchema
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas, StandorteigenschaftenGasSchema
from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom, StandorteigenschaftenStromSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/StandorteigenschaftenSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.STANDORTEIGENSCHAFTEN)
    #: Allgemeine Eigenschaften
    eigenschaften_allgemein: StandorteigenschaftenAllgemein = attrs.field(
        validator=attrs.validators.instance_of(StandorteigenschaftenAllgemein)
    )
    #: Eigenschaften zur Sparte Strom
    eigenschaften_strom: List[StandorteigenschaftenStrom] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(StandorteigenschaftenStrom),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Eigenschaften zur Sparte Gas
    eigenschaften_gas: Optional[StandorteigenschaftenGas] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(StandorteigenschaftenGas)), default=None
    )


class StandorteigenschaftenSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Standorteigenschaften
    """

    class_name = Standorteigenschaften
    # required attributes
    eigenschaften_allgemein = fields.Nested(StandorteigenschaftenAllgemeinSchema, data_key="eigenschaftenAllgemein")

    eigenschaften_strom = fields.List(fields.Nested(StandorteigenschaftenStromSchema), data_key="eigenschaftenStrom")

    # optional attributes
    eigenschaften_gas = fields.Nested(StandorteigenschaftenGasSchema, load_default=None, data_key="eigenschaftenGas")
