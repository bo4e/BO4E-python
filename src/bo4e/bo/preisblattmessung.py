"""
Contains PreisblattMessung class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.preisblatt import Preisblatt, PreisblattSchema
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften, GeraeteeigenschaftenSchema
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class PreisblattMessung(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise des Messstellenbetriebs und damit verbundener Leistungen

    .. HINT::
        `PreisblattMessung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/bo/PreisblattMessungSchema.json>`_

    """

    bo_typ: BoTyp = attr.ib(default=BoTyp.PREISBLATTMESSUNG)
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode = attr.ib(validator=attr.validators.instance_of(Bilanzierungsmethode))
    #: Die Preise gelten für Messlokationen in der angebebenen Netzebene
    messebene: Netzebene = attr.ib(validator=attr.validators.instance_of(Netzebene))

    #: Der Preis betrifft den hier angegebenen Zähler, z.B. einen Drehstromzähler
    zaehler: Geraeteeigenschaften = attr.ib(validator=attr.validators.instance_of(Geraeteeigenschaften))
    # todo: https://github.com/Hochfrequenz/BO4E-python/issues/333

    # optional attributes
    #: Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung
    inklusive_dienstleistungen: Optional[List[Dienstleistungstyp]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Dienstleistungstyp),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )

    #: Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler
    inklusive_geraete: Optional[List[Geraeteeigenschaften]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Geraeteeigenschaften),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )


class PreisblattMessungSchema(PreisblattSchema):
    """
    Schema for de-/serialization of PreisblattMessung
    """

    class_name = PreisblattMessung  # type:ignore[assignment]
    # required attributes
    bilanzierungsmethode = EnumField(Bilanzierungsmethode)
    messebene = EnumField(Netzebene)
    zaehler = fields.Nested(GeraeteeigenschaftenSchema)
    # optional attributes
    inklusive_dienstleistungen = fields.List(EnumField(Dienstleistungstyp))
    inklusive_geraete = fields.List(fields.Nested(GeraeteeigenschaftenSchema))
