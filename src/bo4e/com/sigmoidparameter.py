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
        `Sigmoidparameter JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Sigmoidparameter.json>`_

    """

    A: Optional[Decimal] = None  #: Briefmarke Ortsverteilnetz (EUR/kWh)
    B: Optional[Decimal] = None  #: Wendepunkt für die bepreiste Menge (kW)
    C: Optional[Decimal] = None  #: Exponent (einheitenlos)
    D: Optional[Decimal] = None  #: Briefmarke Transportnetz (EUR/kWh)
