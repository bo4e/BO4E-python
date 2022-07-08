"""
Contains Sigmoidparameter class and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

from bo4e.com.com import COM

# pylint:disable=invalid-name, too-few-public-methods


class Sigmoidparameter(COM):
    """
    Die Sigmoid-Funktion, beispielsweise zur Berechnung eines Leistungspreises hat die Form:
    LP=A/(1+(P/B)^C)+D

    .. raw:: html

        <object data="../_static/images/bo4e/com/Sigmoidparameter.svg" type="image/svg+xml"></object>

    .. HINT::
        `Sigmoidparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Sigmoidparameter.json>`_

    """

    # required attributes
    A: Decimal  #: Briefmarke Ortsverteilnetz (EUR/kWh)
    B: Decimal  #: Wendepunkt für die bepreiste Menge (kW)
    C: Decimal  #: Exponent (einheitenlos)
    D: Decimal  #: Briefmarke Transportnetz (EUR/kWh)

    def calculate(self, leistung: Decimal) -> Decimal:
        """
        calculates LP
        :param leistung: Leistung in Kilowatt
        :return: den Sigmoidparameter LP in EUR/kWh
        """
        return self.A / (1 + (leistung / self.B) ** self.C) + self.D
