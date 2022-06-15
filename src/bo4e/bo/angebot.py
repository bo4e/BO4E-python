"""
Contains Angebot class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.ansprechpartner import Ansprechpartner, AnsprechpartnerSchema
from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.angebotsvariante import Angebotsvariante, AngebotsvarianteSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Angebot(Geschaeftsobjekt):
    """
    Mit diesem BO kann ein Versorgungsangebot zur Strom- oder Gasversorgung oder die Teilnahme an einer Ausschreibung
    übertragen werden. Es können verschiedene Varianten enthalten sein (z.B. ein- und mehrjährige Laufzeit).
    Innerhalb jeder Variante können Teile enthalten sein, die jeweils für eine oder mehrere Marktlokationen erstellt
    werden.

    .. HINT::
        `Angebot JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/AngebotSchema.json>`_

    """

    bo_typ: BoTyp = attrs.field(default=BoTyp.ANGEBOT)
    # required attributes
    #: Eindeutige Nummer des Angebotes
    angebotsnummer: str = attrs.field(validator=attrs.validators.matches_re(r"^\d+$"))
    #: Erstellungsdatum des Angebots
    angebotsdatum: datetime = attrs.field(validator=attrs.validators.instance_of(datetime))
    #: Sparte, für die das Angebot abgegeben wird (Strom/Gas)
    sparte: Sparte = attrs.field(validator=attrs.validators.instance_of(Sparte))
    #: Ersteller des Angebots
    angebotsgeber: Geschaeftspartner = attrs.field(validator=attrs.validators.instance_of(Geschaeftspartner))
    #: Empfänger des Angebots
    angebotsnehmer: Geschaeftspartner = attrs.field(validator=attrs.validators.instance_of(Geschaeftspartner))

    varianten: List[Angebotsvariante] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Angebotsvariante),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    """ Eine oder mehrere Varianten des Angebots mit den Angebotsteilen;
    Ein Angebot besteht mindestens aus einer Variante."""

    # optional attributes
    anfragereferenz: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    """	Referenz auf eine Anfrage oder Ausschreibung;
    Kann dem Empfänger des Angebotes bei Zuordnung des Angebotes zur Anfrage bzw. Ausschreibung helfen."""
    #: Bis zu diesem Zeitpunkt (Tag/Uhrzeit) inklusive gilt das Angebot
    bindefrist: Optional[datetime] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(datetime))
    )
    #: Person, die als Angebotsnehmer das Angebot angenommen hat
    unterzeichner_angebotsnehmer: Optional[Ansprechpartner] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Ansprechpartner))
    )
    #: Person, die als Angebotsgeber das Angebots ausgestellt hat
    unterzeichner_angebotsgeber: Optional[Ansprechpartner] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Ansprechpartner))
    )


class AngebotSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Angebot
    """

    class_name = Angebot

    # required attributes
    angebotsnummer = fields.Str()
    angebotsdatum = fields.DateTime()
    sparte = EnumField(Sparte)
    angebotsgeber = fields.Nested(GeschaeftspartnerSchema)
    angebotsnehmer = fields.Nested(GeschaeftspartnerSchema)
    varianten = fields.List(fields.Nested(AngebotsvarianteSchema))

    # optional attributes
    anfragereferenz = fields.Str(allow_none=True)
    bindefrist = fields.DateTime(allow_none=True)
    unterzeichner_angebotsnehmer = fields.Nested(
        AnsprechpartnerSchema, allow_none=True, data_key="unterzeichnerAngebotsnehmer"
    )
    unterzeichner_angebotsgeber = fields.Nested(
        AnsprechpartnerSchema, allow_none=True, data_key="unterzeichnerAngebotsgeber"
    )
