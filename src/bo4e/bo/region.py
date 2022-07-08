"""
Contains Region class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.regionskriterium import Regionskriterium
from bo4e.enum.botyp import BoTyp


class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Region.svg" type="image/svg+xml"></object>

    .. HINT::
        `Region JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Region.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.REGION
    #: Bezeichnung der Region
    bezeichnung: str

    #: Positivliste der Kriterien zur Definition der Region
    positiv_liste: conlist(Regionskriterium, min_items=1)  # type: ignore[valid-type]

    # optional attributes
    #: Negativliste der Kriterien zur Definition der Region
    negativ_liste: Optional[List[Regionskriterium]] = None
