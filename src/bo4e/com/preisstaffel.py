"""
Contains Preisstaffel and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM
from .sigmoidparameter import Sigmoidparameter

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preisstaffel(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisstaffel.json>`_

    """

    #: Preis pro abgerechneter Mengeneinheit
    einheitspreis: Optional[Decimal] = None
    #: Inklusiver unterer Wert, ab dem die Staffel gilt
    staffelgrenze_von: Optional[Decimal] = None
    #: Exklusiver oberer Wert, bis zu dem die Staffel gilt
    staffelgrenze_bis: Optional[Decimal] = None

    #: Parameter zur Berechnung des Preises anhand der Jahresmenge und weiterer netzbezogener Parameter
    sigmoidparameter: Optional[Sigmoidparameter] = None
