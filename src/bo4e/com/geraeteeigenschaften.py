"""
Contains Geraeteeigenschaften and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.geraetemerkmal import Geraetemerkmal
from ..enum.geraetetyp import Geraetetyp
from .com import COM

# pylint: disable=too-few-public-methods


class Geraeteeigenschaften(COM):
    """
    Mit dieser Komponente werden die Eigenschaften eines Gerätes in Bezug auf den Typ und weitere Merkmale modelliert

    .. raw:: html

        <object data="../_static/images/bo4e/com/Geraeteeigenschaften.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraeteeigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Geraeteeigenschaften.json>`_

    """

    #: Der Typ eines Gerätes, beispielsweise Drehstromzähler
    geraetetyp: Optional[Geraetetyp] = None

    #: Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc..
    geraetemerkmal: Optional[Geraetemerkmal] = None
