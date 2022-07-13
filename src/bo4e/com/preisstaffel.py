"""
Contains Preisstaffel and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

from bo4e.com.com import COM
from bo4e.com.sigmoidparameter import Sigmoidparameter

# pylint: disable=too-few-public-methods


class Preisstaffel(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Preisstaffel.json>`_

    """

    # required attributes
    #: Preis pro abgerechneter Mengeneinheit
    einheitspreis: Decimal
    #: Inklusiver unterer Wert, ab dem die Staffel gilt
    staffelgrenze_von: Decimal
    #: Exklusiver oberer Wert, bis zu dem die Staffel gilt
    staffelgrenze_bis: Decimal

    # optional attributes
    #: Parameter zur Berechnung des Preises anhand der Jahresmenge und weiterer netzbezogener Parameter
    sigmoidparameter: Optional[Sigmoidparameter] = None
