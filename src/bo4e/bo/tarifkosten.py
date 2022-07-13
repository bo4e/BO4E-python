"""
Contains Tarifkosten class
and corresponding marshmallow schema for de-/serialization
"""


from bo4e.bo.kosten import Kosten
from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.enum.botyp import BoTyp

# pylint: disable=too-few-public-methods


class Tarifkosten(Tarifinfo):
    """
    Objekt zur Kommunikation von Kosten, die im Rahmen der Tarifanwendung entstehen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifkosten.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Tarifkosten.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.TARIFKOSTEN
    kosten: Kosten
    """
    Referenz (Link) zu einem Kostenobjekt, in dem die Kosten für die Anwendung
    des Tarifs auf eine Abnahmesituation berechnet wurden
    """

    # there are no optional attributes
