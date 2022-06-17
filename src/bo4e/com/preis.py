"""
Contains Preis class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional


from bo4e.com.com import COM
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods


class Preis(COM):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PreisSchema.json>`_

    """

    # required attributes
    #: Gibt die nominale Höhe des Preises an.
    wert: Decimal
    #: Währungseinheit für den Preis, z.B. Euro oder Ct.
    einheit: Waehrungseinheit
    #: Angabe, für welche Bezugsgröße der Preis gilt. Z.B. kWh.
    bezugswert: Mengeneinheit

    # optional attributes
    #: Gibt den Status des veröffentlichten Preises an
    status: Preisstatus = None
