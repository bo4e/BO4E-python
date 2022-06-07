"""
Contains PreisblattNetnutzung class and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.preisblatt import Preisblatt, PreisblattSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kundengruppe import Kundengruppe
from bo4e.enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class PreisblattNetznutzung(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung der Netznutzungspreise

    .. HINT::
        `PreisblattNetznutzung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattNetznutzungSchema.json>`_

    """

    bo_typ: BoTyp = attrs.field(default=BoTyp.PREISBLATTNETZNUTZUNG)
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode = attrs.field(
        validator=attrs.validators.instance_of(Bilanzierungsmethode)
    )
    #: Die Preise gelten für Marktlokationen in der angebebenen Netzebene
    netzebene: Netzebene = attrs.field(validator=attrs.validators.instance_of(Netzebene))
    kundengruppe: Kundengruppe = attrs.field(validator=attrs.validators.instance_of(Kundengruppe))

    # there are no optional attributes (additionally to those of Preisblatt)


class PreisblattNetznutzungSchema(PreisblattSchema):
    """
    Schema for de-/serialization of PreisblattNetznutzung
    """

    class_name = PreisblattNetznutzung  # type:ignore[assignment]
    # required attributes
    bilanzierungsmethode = EnumField(Bilanzierungsmethode)
    netzebene = EnumField(Netzebene)
    kundengruppe = EnumField(Kundengruppe)
