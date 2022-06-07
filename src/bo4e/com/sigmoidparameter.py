"""
Contains Sigmoidparameter class and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint:disable=invalid-name, too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Sigmoidparameter(COM):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=A/(1+(P/B)^C)+D

    .. HINT::
        `Sigmoidparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/SigmoidparameterSchema.json>`_

    """

    # required attributes
    A: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))  #: Briefmarke Ortsverteilnetz (EUR/kWh)
    B: Decimal = attrs.field(
        validator=attrs.validators.instance_of(Decimal)
    )  #: Wendepunkt für die bepreiste Menge (kW)
    C: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))  #: Exponent (einheitenlos)
    D: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))  #: Briefmarke Transportnetz (EUR/kWh)

    def calculate(self, leistung: Decimal) -> Decimal:
        """
        calculates LP
        :param leistung: Leistung in Kilowatt
        :return: den Sigmoidparameter LP in EUR/kWh
        """
        return self.A / (1 + (leistung / self.B) ** self.C) + self.D


class SigmoidparameterSchema(COMSchema):
    """
    Schema for de-/serialization of Sigmoidparameter.
    """

    class_name = Sigmoidparameter
    # required attributes
    A = fields.Decimal(as_string=True, data_key="A")
    B = fields.Decimal(as_string=True, data_key="B")
    C = fields.Decimal(as_string=True, data_key="C")
    D = fields.Decimal(as_string=True, data_key="D")
