"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein, StandorteigenschaftenAllgemeinSchema
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas, StandorteigenschaftenGasSchema
from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom, StandorteigenschaftenStromSchema
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.STANDORTEIGENSCHAFTEN)
    #: Allgemeine Eigenschaften
    eigenschaften_allgemein: StandorteigenschaftenAllgemein = attr.ib(
        validator=attr.validators.instance_of(StandorteigenschaftenAllgemein)
    )
    #: Eigenschaften zur Sparte Strom
    eigenschaften_strom: List[StandorteigenschaftenStrom] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(StandorteigenschaftenStrom),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Eigenschaften zur Sparte Gas
    eigenschaften_gas: Optional[StandorteigenschaftenGas] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(StandorteigenschaftenGas)), default=None
    )


class StandorteigenschaftenSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Standorteigenschaften
    """

    class_name = Standorteigenschaften
    # required attributes
    eigenschaften_allgemein = fields.Nested(StandorteigenschaftenAllgemeinSchema)

    eigenschaften_strom = fields.List(fields.Nested(StandorteigenschaftenStromSchema))

    # optional attributes
    eigenschaften_gas = fields.Nested(StandorteigenschaftenGasSchema, load_default=None)
