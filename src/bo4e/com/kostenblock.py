"""
Contains Kostenblock and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.kostenposition import Kostenposition, KostenpositionSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Kostenblock(COM):
    """
    Mit dieser Komponente werden mehrere Kostenpositionen zusammengefasst.

    .. HINT::
        `Kostenblock JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/KostenblockSchema.json>`_

    """

    # required attributes
    #: Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    kostenblockbezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))

    # optional attributes
    #: Die Summe aller Kostenpositionen dieses Blocks
    summe_kostenblock: Optional[Betrag] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Betrag))
    )

    kostenpositionen: Optional[List[Kostenposition]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Kostenposition),
                iterable_validator=attrs.validators.instance_of(list),
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
    summe_kostenblock = fields.Nested(BetragSchema, allow_none=True, data_key="summeKostenblock")
    kostenpositionen = fields.List(fields.Nested(KostenpositionSchema), allow_none=True)
