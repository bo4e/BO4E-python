"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.vertrag import Vertrag
from bo4e.enum.botyp import BoTyp


class Buendelvertrag(Geschaeftsobjekt):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. graphviz:: /api/dots/bo4e/bo/Buendelvertrag.dot

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.BUENDELVERTRAG
    #: Die Liste mit den Einzelverträgen zu den Abnahmestellen
    einzelvertraege: conlist(Vertrag, min_items=1)
