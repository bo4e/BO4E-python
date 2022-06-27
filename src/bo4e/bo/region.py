"""
Contains Region class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.regionskriterium import Regionskriterium
from bo4e.enum.botyp import BoTyp


class Region(Geschaeftsobjekt):
    """
    Modellierung einer Region als Menge von Kriterien, die eine Region beschreiben

    .. graphviz:: /api/dots/bo4e/bo/Region.dot

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.REGION
    #: Bezeichnung der Region
    bezeichnung: str

    #: Positivliste der Kriterien zur Definition der Region
    positiv_liste: conlist(Regionskriterium, min_items=1)

    # optional attributes
    #: Negativliste der Kriterien zur Definition der Region
    negativ_liste: List[Regionskriterium] = None
