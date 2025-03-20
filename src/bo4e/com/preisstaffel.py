"""
Contains Preisstaffel and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .sigmoidparameter import Sigmoidparameter

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preisstaffel(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisstaffel.json>`_

    """

    einheitspreis: Optional[Decimal] = None
    """Preis pro abgerechneter Mengeneinheit"""
    staffelgrenze_von: Optional[Decimal] = None
    """Inklusiver unterer Wert, ab dem die Staffel gilt"""
    staffelgrenze_bis: Optional[Decimal] = None
    """Exklusiver oberer Wert, bis zu dem die Staffel gilt"""

    sigmoidparameter: Optional["Sigmoidparameter"] = None
    """Parameter zur Berechnung des Preises anhand der Jahresmenge und weiterer netzbezogener Parameter"""

    artikel_id: Optional[str] = None
    """Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst"""
