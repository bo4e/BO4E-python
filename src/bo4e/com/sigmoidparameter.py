"""
Contains Sigmoidparameter class and corresponding marshmallow schema for de-/serialization
"""


# pylint: disable=too-few-public-methods
from decimal import Decimal

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema


@attr.s(auto_attribs=True, kw_only=True)
class Sigmoidparameter(COM):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=\frac{A}{1+(P/B)^C)}+D
    """

    # required attributes
    A: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Briefmarke Ortsverteilnetz
    B: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Wendepunkt für die bepreiste Menge
    C: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Exponent
    D: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))  #: Briefmarke Transportnetz


class SigmoidparameterSchema(COMSchema):
    """
    Schema for de-/serialization of Sigmoidparameter.
    """

    # required attributes
    A = fields.Decimal(as_string=True)
    B = fields.Decimal(as_string=True)
    C = fields.Decimal(as_string=True)
    D = fields.Decimal(as_string=True)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Sigmoidparameter:
        """Deserialize JSON to Sigmoidparameter object"""
        return Sigmoidparameter(**data)
