"""
Contains Energiemenge class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.verbrauch import Verbrauch
from bo4e.enum.botyp import BoTyp
from bo4e.enum.lokationstyp import Lokationstyp


class Energiemenge(Geschaeftsobjekt):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind

    .. graphviz:: /api/dots/bo4e/bo/Energiemenge.dot

    .. HINT::
        `Energiemenge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Energiemenge.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.ENERGIEMENGE
    #: Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört
    lokations_id: str
    # todo: add validator such that only mess- or marktlokations IDs are accepted + cross check with lokationstyp
    #: Gibt an, ob es sich um eine Markt- oder Messlokation handelt
    lokationstyp: Lokationstyp

    #: Gibt den Verbrauch in einer Zeiteinheit an
    energieverbrauch: conlist(Verbrauch, min_items=1)  # type: ignore[valid-type]
    # there are no optional attributes
