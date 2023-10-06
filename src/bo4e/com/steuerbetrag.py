"""
Contains Steuerbetrag class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.steuerkennzeichen import Steuerkennzeichen
from bo4e.enum.waehrungscode import Waehrungscode

# pylint: disable=too-few-public-methods


class Steuerbetrag(COM):
    """
    Abbildung eines Steuerbetrages.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Steuerbetrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Steuerbetrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Steuerbetrag.json>`_

    """

    #: Kennzeichnung des Steuersatzes, bzw. Verfahrens.
    steuerkennzeichen: Optional[Steuerkennzeichen] = None
    #: Nettobetrag für den die Steuer berechnet wurde. Z.B. 100
    basiswert: Optional[Decimal] = None
    #: Aus dem Basiswert berechnete Steuer. Z.B. 19 (bei UST_19)
    steuerwert: Optional[Decimal] = None
    #: Währung. Z.B. Euro.
    waehrung: Optional[Waehrungscode] = None
