"""
Contains Angebotsvariante and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.angebotsteil import Angebotsteil, AngebotsteilSchema
from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.enum.angebotsstatus import Angebotsstatus
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Angebotsvariante(COM):
    """
    Führt die verschiedenen Ausprägungen der Angebotsberechnung auf
    """

    # required attributes
    #: Gibt den Status eines Angebotes an.
    angebotsstatus: Angebotsstatus = attr.ib(validator=attr.validators.instance_of(Angebotsstatus))

    #: Datum der Erstellung der Angebotsvariante
    erstellungsdatum: datetime = attr.ib(validator=attr.validators.instance_of(datetime))

    #: Bis zu diesem Zeitpunkt gilt die Angebotsvariante
    bindefrist: datetime = attr.ib(validator=attr.validators.instance_of(datetime))

    teile: List[Angebotsteil] = attr.ib(
        validator=[
            attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(Angebotsteil),
                iterable_validator=attr.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )
    """
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.
    """

    # optional attributes
    #: Aufsummierte Wirkarbeitsmenge aller Angebotsteile
    gesamtmenge: Optional[Menge] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Menge))
    )
    # todo: write a validator for this: https://github.com/Hochfrequenz/BO4E-python/issues/320
    #: Aufsummierte Kosten aller Angebotsteile
    gesamtkosten: Optional[Betrag] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Betrag))
    )


class AngebotsvarianteSchema(COMSchema):
    """
    Schema for de-/serialization of Angebotsvariante
    """

    class_name = Angebotsvariante
    # required attributes
    angebotsstatus = EnumField(Angebotsstatus)
    erstellungsdatum = fields.DateTime()
    bindefrist = fields.DateTime()
    teile = fields.List(fields.Nested(AngebotsteilSchema))

    # optional attributes
    gesamtmenge = fields.Nested(MengeSchema, allow_none=True)
    gesamtkosten = fields.Nested(BetragSchema, allow_none=True)
