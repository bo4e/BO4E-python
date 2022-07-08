"""
Contains Steuerbetrag class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

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

    # required attributes
    #: Kennzeichnung des Steuersatzes, bzw. Verfahrens.
    steuerkennzeichen: Steuerkennzeichen
    #: Nettobetrag für den die Steuer berechnet wurde. Z.B. 100
    basiswert: Decimal
    #: Aus dem Basiswert berechnete Steuer. Z.B. 19 (bei UST_19)
    steuerwert: Decimal
    #: Währung. Z.B. Euro.
    waehrung: Waehrungscode
