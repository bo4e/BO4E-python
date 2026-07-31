"""
Contains Sigmoidparameter class
"""

from decimal import Decimal
from typing import Annotated, Literal

from pydantic import Field

from ..enum.comtyp import ComTyp
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

    typ: Annotated[Literal[ComTyp.SIGMOIDPARAMETER], Field(alias="_typ")] = ComTyp.SIGMOIDPARAMETER

    A: Decimal | None = None
    """Briefmarke Ortsverteilnetz (EUR/kWh)"""
    B: Decimal | None = None
    """Wendepunkt für die bepreiste Menge (kW)"""
    C: Decimal | None = None
    """Exponent (einheitenlos)"""
    D: Decimal | None = None
    """Briefmarke Transportnetz (EUR/kWh)"""
