"""
Contains Preis class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

from bo4e.com.com import COM
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods


class Preis(COM):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. graphviz:: /api/dots/bo4e/com/Preis.dot

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
