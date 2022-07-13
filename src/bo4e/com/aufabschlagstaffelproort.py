"""
Contains AufAbschlagstaffelProOrt class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

from bo4e.com.com import COM

# pylint: disable=too-few-public-methods


class AufAbschlagstaffelProOrt(COM):
    """
    Gibt den Wert eines Auf- oder Abschlags und dessen Staffelgrenzen an

    .. raw:: html

        <object data="../_static/images/bo4e/com/AufAbschlagstaffelProOrt.svg" type="image/svg+xml"></object>

    .. HINT::
        `AufAbschlagstaffelProOrt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagstaffelProOrt.json>`_

    """

    # required attributes
    #: Der Wert für den Auf- oder Abschlag.
    wert: Decimal
    #: Unterer Wert, ab dem die Staffel gilt.
    staffelgrenze_von: Decimal
    #: Oberer Wert, bis zu dem die Staffel gilt.
    staffelgrenze_bis: Decimal
