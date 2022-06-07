"""
Contains PreisblattKonzessionsabgabe class and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.preisblatt import Preisblatt, PreisblattSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kundengruppeka import KundengruppeKA


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class PreisblattKonzessionsabgabe(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattKonzessionsabgabeSchema.json>`_

    """

    bo_typ: BoTyp = attrs.field(default=BoTyp.PREISBLATTKONZESSIONSABGABE)
    # required attributes (additional to those of Preisblatt)
    #: Kundegruppe anhand derer die Höhe der Konzessionabgabe festgelegt ist
    kundengruppe_k_a: KundengruppeKA = attrs.field(validator=attrs.validators.instance_of(KundengruppeKA))

    # there are no optional attributes (additionally to those of Preisblatt)


class PreisblattKonzessionsabgabeSchema(PreisblattSchema):
    """
    Schema for de-/serialization of PreisblattKonzessionsabgabe
    """

    class_name = PreisblattKonzessionsabgabe  # type:ignore[assignment]
    # required attributes
    kundengruppe_k_a = EnumField(KundengruppeKA, data_key="kundengruppeKA")
