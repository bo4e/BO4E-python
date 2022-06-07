"""
Contains PreisblattHardware class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.preisblatt import Preisblatt, PreisblattSchema
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften, GeraeteeigenschaftenSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class PreisblattHardware(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für zusätzliche Hardware

    .. HINT::
        `PreisblattHardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattHardwareSchema.json>`_

    """

    bo_typ: BoTyp = attrs.field(default=BoTyp.PREISBLATTHARDWARE)
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode = attrs.field(
        validator=attrs.validators.instance_of(Bilanzierungsmethode)
    )
    #: Die Preise gelten für Messlokationen in der angebebenen Netzebene
    messebene: Netzebene = attrs.field(validator=attrs.validators.instance_of(Netzebene))

    #: Der Preis betriftt das hier angegebene Gerät, z.B. ein Tarifschaltgerät
    basisgeraet: Geraeteeigenschaften = attrs.field(validator=attrs.validators.instance_of(Geraeteeigenschaften))

    # optional attributes
    #: Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung
    inklusive_dienstleistungen: Optional[List[Dienstleistungstyp]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Dienstleistungstyp),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )

    #: Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler
    inklusive_geraete: Optional[List[Geraeteeigenschaften]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Geraeteeigenschaften),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )


class PreisblattHardwareSchema(PreisblattSchema):
    """
    Schema for de-/serialization of PreisblattHardware
    """

    class_name = PreisblattHardware  # type:ignore[assignment]
    # required attributes
    bilanzierungsmethode = EnumField(Bilanzierungsmethode)
    messebene = EnumField(Netzebene)
    basisgeraet = fields.Nested(GeraeteeigenschaftenSchema)
    # optional attributes
    inklusive_dienstleistungen = fields.List(EnumField(Dienstleistungstyp), data_key="inklusiveDienstleistungen")
    inklusive_geraete = fields.List(fields.Nested(GeraeteeigenschaftenSchema), data_key="inklusiveGeraete")
