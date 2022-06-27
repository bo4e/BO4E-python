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

    .. graphviz:: /api/dots/bo4e/com/AufAbschlagstaffelProOrt.dot

    """

    # required attributes
    #: Der Wert für den Auf- oder Abschlag.
    wert: Decimal
    #: Unterer Wert, ab dem die Staffel gilt.
    staffelgrenze_von: Decimal
    #: Oberer Wert, bis zu dem die Staffel gilt.
    staffelgrenze_bis: Decimal
