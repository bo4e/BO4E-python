"""
Contains Angebotsteil class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields

from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.angebotsposition import Angebotsposition
from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.zeitraum import Zeitraum
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Angebotsteil(COM):
    """
    Mit dieser Komponente wird ein Teil einer Angebotsvariante abgebildet.
    Hier werden alle Angebotspositionen aggregiert.
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.

    .. HINT::
        `Angebotsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AngebotsteilSchema.json>`_

    """

    # required attributes
    #: Einzelne Positionen, die zu diesem Angebotsteil gehören
    positionen: List[Angebotsposition] = attrs.field(
        validator=[
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Angebotsposition),
                iterable_validator=attrs.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )

    # optional attributes
    #: Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    anfrage_subreferenz: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    lieferstellenangebotsteil: Optional[List[Marktlokation]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Marktlokation),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )
    """
    Marktlokationen, für die dieses Angebotsteil gilt, falls vorhanden.
    Durch die Marktlokation ist auch die Lieferadresse festgelegt
    """
    #: Summe der Verbräuche aller in diesem Angebotsteil eingeschlossenen Lieferstellen
    gesamtmengeangebotsteil: Optional[Menge] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Menge))
    )
    #: Summe der Jahresenergiekosten aller in diesem Angebotsteil enthaltenen Lieferstellen
    gesamtkostenangebotsteil: Optional[Betrag] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Betrag))
    )
    #: Hier kann der Belieferungszeitraum angegeben werden, für den dieser Angebotsteil gilt
    lieferzeitraum: Optional[Zeitraum] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum))
    )


class AngebotsteilSchema(COMSchema):
    """
    Schema for de-/serialization of Angebotsteil.
    """

    class_name = Angebotsteil
    # required attributes
    positionen = fields.List(fields.Nested(AngebotspositionSchema))

    # optional attributes
    anfrage_subreferenz = fields.Str(load_default=None, data_key="anfrageSubreferenz")
    lieferstellenangebotsteil = fields.List(fields.Nested(MarktlokationSchema), load_default=None)
    gesamtmengeangebotsteil = fields.Nested(MengeSchema, load_default=None)
    gesamtkostenangebotsteil = fields.Nested(BetragSchema, load_default=None)
    lieferzeitraum = fields.Nested(ZeitraumSchema, load_default=None)
