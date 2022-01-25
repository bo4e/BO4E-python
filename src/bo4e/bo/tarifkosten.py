"""
Contains Tarifkosten class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields

from bo4e.bo.kosten import Kosten, KostenSchema
from bo4e.bo.tarifinfo import Tarifinfo, TarifinfoSchema
from bo4e.enum.botyp import BoTyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Tarifkosten(Tarifinfo):
    """
    Objekt zur Kommunikation von Kosten, die im Rahmen der Tarifanwendung entstehen

    .. HINT::
        `Tarifkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/TarifkostenSchema.json>`_
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.TARIFKOSTEN)
    kosten: Kosten = attr.ib(validator=attr.validators.instance_of(Kosten))
    """
    Referenz (Link) zu einem Kostenobjekt, in dem die Kosten für die Anwendung
    des Tarifs auf eine Abnahmesituation berechnet wurden
    """

    # there are no optional attributes


class TarifkostenSchema(TarifinfoSchema):
    """
    Schema for de-/serialization of Tarifkosten.
    """

    # class_name is needed to use the correct schema for deserialization.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Tarifkosten  # type:ignore[assignment]

    # required attributes
    kosten = fields.Nested(KostenSchema)
