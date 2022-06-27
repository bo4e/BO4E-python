"""
Contains Geraeteeigenschaften and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods


class Geraeteeigenschaften(COM):
    """
    Mit dieser Komponente werden die Eigenschaften eines Gerätes in Bezug auf den Typ und weitere Merkmale modelliert

    .. graphviz:: /api/dots/bo4e/com/Geraeteeigenschaften.dot

    """

    # required attributes
    #: Der Typ eines Gerätes, beispielsweise Drehstromzähler
    geraetetyp: Geraetetyp

    # optional attributes
    #: Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc..
    geraetemerkmal: Geraetemerkmal = None
