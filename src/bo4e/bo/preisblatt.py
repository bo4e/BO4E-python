"""
Contains Preisblatt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.marktteilnehmer import Marktteilnehmer
from bo4e.com.preisposition import Preisposition
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Preisblatt(Geschaeftsobjekt):
    """
    Das allgemeine Modell zur Abbildung von Preisen;
    Davon abgeleitet können, über die Zuordnung identifizierender Merkmale, spezielle Preisblatt-Varianten modelliert
    werden.

    Die jeweiligen Sätze von Merkmalen sind in der Grafik ergänzt worden und stellen jeweils eine Ausprägung für die
    verschiedenen Anwendungsfälle der Preisblätter dar.

    .. HINT::
        `Preisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.PREISBLATT
    #: Eine Bezeichnung für das Preisblatt
    bezeichnung: str
    #: Preisblatt gilt für angegebene Sparte
    sparte: Sparte
    #: Merkmal, das anzeigt, ob es sich um vorläufige oder endgültige Preise handelt
    preisstatus: Preisstatus
    #: Der Zeitraum für den der Preis festgelegt ist
    gueltigkeit: Zeitraum
    #: Die einzelnen Positionen, die mit dem Preisblatt abgerechnet werden können. Z.B. Arbeitspreis, Grundpreis etc
    preispositionen: List[Preisposition] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Preisposition),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Der Netzbetreiber, der die Preise veröffentlicht hat
    herausgeber: Optional[Marktteilnehmer] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Marktteilnehmer))
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
