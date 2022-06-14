"""
Contains Preisstaffel and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

import attrs
from marshmallow import fields

from bo4e.com.com import COM
from bo4e.com.sigmoidparameter import Sigmoidparameter


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Preisstaffel(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PreisstaffelSchema.json>`_

    """

    # required attributes
    #: Preis pro abgerechneter Mengeneinheit
    einheitspreis: Decimal
    #: Inklusiver unterer Wert, ab dem die Staffel gilt
    staffelgrenze_von: Decimal
    #: Exklusiver oberer Wert, bis zu dem die Staffel gilt
    staffelgrenze_bis: Decimal

    # optional attributes
    #: Parameter zur Berechnung des Preises anhand der Jahresmenge und weiterer netzbezogener Parameter
    sigmoidparameter: Optional[Sigmoidparameter] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Sigmoidparameter))
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
