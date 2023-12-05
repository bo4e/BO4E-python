"""
Contains Sigmoidparameter class and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM

# pylint:disable=invalid-name, too-few-public-methods


@postprocess_docstring
class Sigmoidparameter(COM):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=A/(1+(P/B)^C)+D

    .. raw:: html

        <object data="../_static/images/bo4e/com/Sigmoidparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Sigmoidparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Sigmoidparameter.json>`_

    """

    A: Optional[Decimal] = None  #: Briefmarke Ortsverteilnetz (EUR/kWh)
    B: Optional[Decimal] = None  #: Wendepunkt für die bepreiste Menge (kW)
    C: Optional[Decimal] = None  #: Exponent (einheitenlos)
    D: Optional[Decimal] = None  #: Briefmarke Transportnetz (EUR/kWh)

    def calculate(self, leistung: Decimal) -> Decimal:
        """
        calculates LP
        :param leistung: Leistung in Kilowatt
        :return: den Sigmoidparameter LP in EUR/kWh
        """
        if self.A is None or self.B is None or self.C is None or self.D is None:
            raise ValueError("Sigmoidparameter is not fully defined")
        return self.A / (1 + (leistung / self.B) ** self.C) + self.D
