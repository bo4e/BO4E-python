"""
Contains Fremdkostenblock class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.fremdkostenposition import Fremdkostenposition, FremdkostenpositionSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Fremdkostenblock(COM):
    """
    Komponente zur Abbildung eines Kostenblocks in den Fremdkosten

    .. HINT::
        `Fremdkostenblock JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/FremdkostenblockSchema.json>`_

    """

    # required attributes
    #: Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    kostenblockbezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))

    # optional attributes
    kostenpositionen: Optional[List[Fremdkostenposition]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Fremdkostenposition),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )
    """
    Hier sind die Details zu einer Kostenposition aufgeführt. Z.B.:
    Alliander Netz Heinsberg GmbH, 2018-02-01, 2019-01-01, Arbeitspreis HT, 3.660 kWh,
    5,8200 ct/kWh, 213,01 €
    """

    #: Die Summe aller Kostenpositionen dieses Blocks
    summe_kostenblock: Optional[Betrag] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Betrag))
    )
    # todo: write validator fo this sum, see https://github.com/Hochfrequenz/BO4E-python/issues/324


class FremdkostenblockSchema(COMSchema):
    """
    Schema for de-/serialization of Fremdkostenblock
    """

    class_name = Fremdkostenblock
    # required attributes
    kostenblockbezeichnung = fields.Str()

    # optional attributes
    kostenpositionen = fields.List(fields.Nested(FremdkostenpositionSchema), load_default=None)
    summe_kostenblock = fields.Nested(BetragSchema, load_default=None, data_key="summeKostenblock")
