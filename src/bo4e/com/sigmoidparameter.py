"""
Contains Sigmoidparameter class and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema


# pylint:disable=invalid-name, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Sigmoidparameter(COM):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=A/(1+(P/B)^C)+D
    """

    # required attributes
    A: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Briefmarke Ortsverteilnetz (EUR/kWh)
    B: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Wendepunkt für die bepreiste Menge (kW)
    C: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Exponent (einheitenlos)
    D: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Briefmarke Transportnetz (EUR/kWh)

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
    A = fields.Decimal(as_string=True)
    B = fields.Decimal(as_string=True)
    C = fields.Decimal(as_string=True)
    D = fields.Decimal(as_string=True)
