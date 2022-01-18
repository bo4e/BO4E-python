"""
Contains Kosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.kostenblock import Kostenblock, KostenblockSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kostenklasse import Kostenklasse
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Kosten(Geschaeftsobjekt):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.KOSTEN)
    #: Klasse der Kosten, beispielsweise Fremdkosten
    kostenklasse: Kostenklasse = attr.ib(validator=attr.validators.instance_of(Kostenklasse))
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Zeitraum = attr.ib(validator=attr.validators.instance_of(Zeitraum))
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: List[Kostenblock] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Kostenblock),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: List[Betrag] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Betrag),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )


class KostenSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Kosten
    """

    # class_name is needed to use the correct schema for deserialisation.
    # see function `deserialize` in geschaeftsobjekt.py
    class_name = Kosten

    kostenklasse = EnumField(Kostenklasse)
    gueltigkeit = fields.Nested(ZeitraumSchema)
    kostenbloecke = fields.List(fields.Nested(KostenblockSchema))
    # optional attributes
    summe_kosten = fields.List(fields.Nested(BetragSchema), load_default=None)
