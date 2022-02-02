"""
Contains Preisstaffel and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.sigmoidparameter import Sigmoidparameter, SigmoidparameterSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Preisstaffel(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PreisstaffelSchema.json>`_

    """

    # required attributes
    #: Preis pro abgerechneter Mengeneinheit
    einheitspreis: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Inklusiver unterer Wert, ab dem die Staffel gilt
    staffelgrenze_von: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Exklusiver oberer Wert, bis zu dem die Staffel gilt
    staffelgrenze_bis: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))

    # optional attributes
    #: Parameter zur Berechnung des Preises anhand der Jahresmenge und weiterer netzbezogener Parameter
    sigmoidparameter: Optional[Sigmoidparameter] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Sigmoidparameter))
    )


class PreisstaffelSchema(COMSchema):
    """
    Schema for de-/serialization of Preisstaffel
    """

    class_name = Preisstaffel
    # required attributes
    einheitspreis = fields.Decimal(as_string=True)
    staffelgrenze_von = fields.Decimal(as_string=True, data_key="staffelgrenzeVon")
    staffelgrenze_bis = fields.Decimal(as_string=True, data_key="staffelgrenzeBis")

    # optional attributes
    sigmoidparameter = fields.Nested(SigmoidparameterSchema, load_default=None)
