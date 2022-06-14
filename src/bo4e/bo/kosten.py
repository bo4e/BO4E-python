"""
Contains Kosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.betrag import Betrag
from bo4e.com.kostenblock import Kostenblock
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kostenklasse import Kostenklasse
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Kosten(Geschaeftsobjekt):
    """
    Dieses BO wird zur Übertagung von hierarchischen Kostenstrukturen verwendet.
    Die Kosten werden dabei in Kostenblöcke und diese wiederum in Kostenpositionen strukturiert.

    .. HINT::
        `Kosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/KostenSchema.json>`_"

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.KOSTEN
    #: Klasse der Kosten, beispielsweise Fremdkosten
    kostenklasse: Kostenklasse
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Zeitraum
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: List[Kostenblock] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Kostenblock),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: List[Betrag] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Betrag),
                iterable_validator=attrs.validators.instance_of(list),
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
    summe_kosten = fields.List(fields.Nested(BetragSchema), load_default=None, data_key="summeKosten")
