"""
Contains Angebotsteil class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attr
from marshmallow import fields

from bo4e.bo.marktlokation import Marktlokation, MarktlokationSchema
from bo4e.com.angebotsposition import Angebotsposition, AngebotspositionSchema
from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Angebotsteil(COM):
    """
    Mit dieser Komponente wird ein Teil einer Angebotsvariante abgebildet.
    Hier werden alle Angebotspositionen aggregiert.
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.
    """

    # required attributes
    #: Einzelne Positionen, die zu diesem Angebotsteil gehören
    positionen: List[Angebotsposition] = attr.ib(
        validator=[
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Angebotsposition),
                iterable_validator=attr.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )

    # optional attributes
    #: Identifizierung eines Subkapitels einer Anfrage, beispielsweise das Los einer Ausschreibung
    anfrage_subreferenz: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    lieferstellenangebotsteil: Optional[List[Marktlokation]] = attr.ib(
        default=None,
        validator=attr.validators.optional(
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Marktlokation),
                iterable_validator=attr.validators.instance_of(list),
            )
        ),
    )
    """
    Marktlokationen, für die dieses Angebotsteil gilt, falls vorhanden.
    Durch die Marktlokation ist auch die Lieferadresse festgelegt
    """
    #: Summe der Verbräuche aller in diesem Angebotsteil eingeschlossenen Lieferstellen
    gesamtmengeangebotsteil: Optional[Menge] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Menge))
    )
    #: Summe der Jahresenergiekosten aller in diesem Angebotsteil enthaltenen Lieferstellen
    gesamtkostenangebotsteil: Optional[Betrag] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Betrag))
    )
    #: Hier kann der Belieferungszeitraum angegeben werden, für den dieser Angebotsteil gilt
    lieferzeitraum: Optional[Zeitraum] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Zeitraum))
    )


class AngebotsteilSchema(COMSchema):
    """
    Schema for de-/serialization of Angebotsteil.
    """

    class_name = Angebotsteil
    # required attributes
    positionen = fields.List(fields.Nested(AngebotspositionSchema))

    # optional attributes
    anfrage_subreferenz = fields.Str(load_default=None)
    lieferstellenangebotsteil = fields.List(fields.Nested(MarktlokationSchema), load_default=None)
    gesamtmengeangebotsteil = fields.Nested(MengeSchema, load_default=None)
    gesamtkostenangebotsteil = fields.Nested(BetragSchema, load_default=None)
    lieferzeitraum = fields.Nested(ZeitraumSchema, load_default=None)
