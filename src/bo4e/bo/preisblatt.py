"""
Contains Preisblatt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.marktteilnehmer import Marktteilnehmer, MarktteilnehmerSchema
from bo4e.com.preisposition import Preisposition, PreispositionSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Preisblatt(Geschaeftsobjekt):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet können, über die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen Sätze von Merkmalen sind in der Grafik ergänzt worden und stellen jeweils eine Ausprägung für die
    verschiedenen Anwendungsfälle der Preisblätter dar.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.PREISBLATT)
    #: Eine Bezeichnung für das Preisblatt
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Preisblatt gilt für angegebene Sparte
    sparte: Sparte = attr.ib(validator=attr.validators.instance_of(Sparte))
    #: Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt
    preisstatus: Preisstatus = attr.ib(validator=attr.validators.instance_of(Preisstatus))
    #: Der Zeitraum für den der Preis festgelegt ist
    gueltigkeit: Zeitraum = attr.ib(validator=attr.validators.instance_of(Zeitraum))
    #: Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc
    preispositionen: List[Preisposition] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Preisposition),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Der Netzbetreiber, der die Preise veröffentlicht hat
    herausgeber: Optional[Marktteilnehmer] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Marktteilnehmer))
    )


class PreisblattSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Preisblatt
    """

    class_name = Preisblatt
    # required attributes
    bezeichnung = fields.Str()
    sparte = EnumField(Sparte)
    preisstatus = EnumField(Preisstatus)
    gueltigkeit = fields.Nested(ZeitraumSchema)
    preispositionen = fields.List(fields.Nested(PreispositionSchema))

    # optional attributes

    herausgeber = fields.Nested(MarktteilnehmerSchema, load_default=None)
