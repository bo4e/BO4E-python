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

    .. graphviz:: /api/dots/bo4e/com/Betrag.dot

    """

    # required attributes
    wert: Decimal  #: Gibt den Betrag des Preises an.
    waehrung: Waehrungscode  #: Die entsprechende Waehrung
