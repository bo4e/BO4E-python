"""
Contains Fremdkostenblock class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.fremdkostenposition import Fremdkostenposition, FremdkostenpositionSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Fremdkostenblock(COM):
    """
    Komponente zur Abbildung eines Kostenblocks in den Fremdkosten
    """

    # required attributes
    #: Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc.
    kostenblockbezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))

    # optional attributes
    kostenpositionen: Optional[List[Fremdkostenposition]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Fremdkostenposition),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    """
    Hier sind die Details zu einer Kostenposition aufgeführt. Z.B.:
    Alliander Netz Heinsberg GmbH, 2018-02-01, 2019-01-01, Arbeitspreis HT, 3.660 kWh,
    5,8200 ct/kWh, 213,01 €
    """

    #: Die Summe aller Kostenpositionen dieses Blocks
    summe_kostenblock: Optional[Betrag] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Betrag))
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
    summe_kostenblock = fields.Nested(BetragSchema, load_default=None)
