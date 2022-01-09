"""
Contains Kostenblock and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.kostenposition import Kostenposition, KostenpositionSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Kostenblock(COM):
    """
    Mit dieser Komponente werden mehrere Kostenpositionen zusammengefasst.
    """

    # required attributes
    #: Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    kostenblockbezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))

    # optional attributes
    #: Die Summe aller Kostenpositionen dieses Blocks
    summe_kostenblock: Optional[Betrag] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Betrag))
    )

    kostenpositionen: Optional[List[Kostenposition]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Kostenposition),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    """
    Hier sind die Details zu einer Kostenposition aufgeführt. Z.B.:
    Alliander Netz Heinsberg GmbH, 01.02.2018, 31.12.2018, Arbeitspreis HT, 3.660 kWh, 5,8200 ct/kWh, 213,01 €
    """


class KostenblockSchema(COMSchema):
    """
    Schema for de-/serialization of Kostenblock
    """

    class_name = Kostenblock
    # required attributes
    kostenblockbezeichnung = fields.Str()
    # optional attributes
    summe_kostenblock = fields.Nested(BetragSchema, allow_none=True)
    kostenpositionen = fields.List(fields.Nested(KostenpositionSchema), allow_none=True)
