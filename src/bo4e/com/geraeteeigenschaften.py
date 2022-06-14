"""
Contains Geraeteeigenschaften and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional


from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods


class Geraeteeigenschaften(COM):
    """
    Mit dieser Komponente werden die Eigenschaften eines Gerätes in Bezug auf den Typ und weitere Merkmale modelliert

    .. HINT::
        `Geraeteeigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/GeraeteeigenschaftenSchema.json>`_

    """

    # required attributes
    #: Der Typ eines Gerätes, beispielsweise Drehstromzähler
    geraetetyp: Geraetetyp

    # optional attributes
    #: Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc..
    geraetemerkmal: Geraetemerkmal = None
