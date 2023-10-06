"""
Contains Geraet class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp

# pylint: disable=too-few-public-methods


class Geraet(Geschaeftsobjekt):
    """
    Mit diesem BO werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Geraet.json>`_

    """

    #: Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    geraetenummer: Optional[str] = None
    #: Bezeichnung des Geräts
    bezeichnung: Optional[str] = None
    #: Der Typ eines Gerätes, beispielsweise Drehstromzähler
    geraetetyp: Optional[Geraetetyp] = None
    #: Weitere Merkmale des Geräts, zum Beispiel Mehrtarif, Eintarif etc..
    geraetemerkmal: Optional[Geraetemerkmal] = None
