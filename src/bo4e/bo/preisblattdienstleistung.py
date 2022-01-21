"""
Contains PreisblattDienstleistung class and corresponding marshmallow schema for de-/serialization
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


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class PreisblattDienstleistung(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für wahlfreie Dienstleistungen
    """

    bo_typ: BoTyp = attr.ib(default=BoTyp.PREISBLATTDIENSTLEISTUNG)
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode = attr.ib(validator=attr.validators.instance_of(Bilanzierungsmethode))
    #: Die Preise gelten für Messlokationen in der angebebenen Netzebene
    basisdienstleistung: Dienstleistungstyp = attr.ib(validator=attr.validators.instance_of(Dienstleistungstyp))

    # optional attributes
    #: Hier kann der Preis auf bestimmte Geräte eingegrenzt werden. Z.B. auf die Zählergröße
    geraetedetails: Optional[Geraeteeigenschaften] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Geraeteeigenschaften))
    )

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


class PreisblattMessungSchema(PreisblattSchema):
    """
    Schema for de-/serialization of PreisblattMessung
    """

    class_name = PreisblattDienstleistung  # type:ignore[assignment]
    # required attributes
    bilanzierungsmethode = EnumField(Bilanzierungsmethode)
    basisdienstleistung = EnumField(Dienstleistungstyp)

    # optional attributes
    inklusive_dienstleistungen = fields.List(EnumField(Dienstleistungstyp))
    geraetedetails = fields.Nested(GeraeteeigenschaftenSchema)
