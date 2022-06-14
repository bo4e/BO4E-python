"""
Contains Buendelvertrag class and corresponding marshmallow schema for de-/serialization
"""
from typing import List


from marshmallow import fields

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.vertrag import Vertrag
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
from pydantic import conlist


class Buendelvertrag(Geschaeftsobjekt):
    """
    Abbildung eines Bündelvertrags.
    Es handelt sich hierbei um eine Liste von Einzelverträgen, die in einem Vertragsobjekt gebündelt sind.

    .. HINT::
        `Buendelvertrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/BuendelvertragSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.BUENDELVERTRAG
    #: Die Liste mit den Einzelverträgen zu den Abnahmestellen
    einzelvertraege: conlist(Vertrag, min_items=1)
