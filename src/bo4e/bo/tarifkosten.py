"""
Contains Tarifkosten class
and corresponding marshmallow schema for de-/serialization
"""
import attrs
from marshmallow import fields

from bo4e.bo.kosten import Kosten
from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.enum.botyp import BoTyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Tarifkosten(Tarifinfo):
    """
    Objekt zur Kommunikation von Kosten, die im Rahmen der Tarifanwendung entstehen

    .. HINT::
        `Tarifkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/TarifkostenSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp
    kosten: Kosten
    """
    Referenz (Link) zu einem Kostenobjekt, in dem die Kosten für die Anwendung
    des Tarifs auf eine Abnahmesituation berechnet wurden
    """

    # there are no optional attributes
