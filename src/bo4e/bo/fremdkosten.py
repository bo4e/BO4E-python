"""
Contains Fremdkosten class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.fremdkostenblock import Fremdkostenblock, FremdkostenblockSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.botyp import BoTyp


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Fremdkosten(Geschaeftsobjekt):
    """
    Mit diesem BO werden die Fremdkosten, beispielsweise für eine Angebotserstellung oder eine Rechnungsprüfung,
    übertragen.
    Die Fremdkosten enthalten dabei alle Kostenblöcke, die von anderen Marktteilnehmern oder Instanzen erhoben werden.

    .. HINT::
        `Fremdkosten JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/FremdkostenSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.FREMDKOSTEN)
    #: Für diesen Zeitraum wurden die Kosten ermittelt
    gueltigkeit: Zeitraum = attrs.field(validator=attrs.validators.instance_of(Zeitraum))
    # optional attributes
    #: Die Gesamtsumme über alle Kostenblöcke und -positionen
    summe_kosten: Optional[Betrag] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Betrag)), default=None
    )
    #: In Kostenblöcken werden Kostenpositionen zusammengefasst. Beispiele: Netzkosten, Umlagen, Steuern etc
    kostenbloecke: Optional[List[Fremdkostenblock]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Fremdkostenblock),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )


class FremdkostenSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Fremdkosten
    """

    class_name = Fremdkosten
    # required attributes
    gueltigkeit = fields.Nested(ZeitraumSchema)

    # optional attributes
    summe_kosten = fields.Nested(BetragSchema, load_default=None, data_key="summeKosten")
    kostenbloecke = fields.List(fields.Nested(FremdkostenblockSchema), load_default=None)
