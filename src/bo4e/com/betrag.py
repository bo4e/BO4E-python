"""
Contains Betrag class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

from bo4e.com.com import COM
from bo4e.enum.waehrungscode import Waehrungscode

# pylint: disable=too-few-public-methods


class Betrag(COM):
    """
    Die Komponente wird dazu verwendet, Summenbeträge (beispielsweise in Angeboten und Rechnungen) als Geldbeträge
    abzubilden. Die Einheit ist dabei immer die Hauptwährung also Euro, Dollar etc…

    .. raw:: html

        <object data="../_static/images/bo4e/com/Betrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Betrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Betrag.json>`_

    """

    # required attributes
    wert: Decimal  #: Gibt den Betrag des Preises an.
    waehrung: Waehrungscode  #: Die entsprechende Waehrung
