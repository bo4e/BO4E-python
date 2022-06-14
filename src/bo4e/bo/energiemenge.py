"""
Contains Energiemenge class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.verbrauch import Verbrauch
from bo4e.enum.botyp import BoTyp
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
from pydantic import conlist


class Energiemenge(Geschaeftsobjekt):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind

    .. HINT::
        `Energiemenge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/EnergiemengeSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.ENERGIEMENGE
    #: Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört
    lokations_id: str
    # todo: add validator such that only mess- or marktlokations IDs are accepted + cross check with lokationstyp
    #: Gibt an, ob es sich um eine Markt- oder Messlokation handelt
    lokationstyp: Lokationstyp

    #: Gibt den Verbrauch in einer Zeiteinheit an
    energieverbrauch: conlist(Verbrauch, min_items=1)
    # there are no optional attributes
