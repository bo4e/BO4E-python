"""
Contains Rechnung class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.rechnungsposition import Rechnungsposition, RechnungspositionSchema
from bo4e.com.steuerbetrag import Steuerbetrag, SteuerbetragSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.rechnungsstatus import Rechnungsstatus
from bo4e.enum.rechnungstyp import Rechnungstyp


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Rechnung(Geschaeftsobjekt):
    """
    Modell für die Abbildung von Rechnungen im Kontext der Energiewirtschaft;
    Ausgehend von diesem Basismodell werden weitere spezifische Formen abgeleitet.

    .. HINT::
        `Rechnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/RechnungSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.RECHNUNG)
    storno: bool = attrs.field(validator=attrs.validators.instance_of(bool))
    """
    Kennzeichnung, ob es sich um eine Stornorechnung handelt;
    im Falle "true" findet sich im Attribut "originalrechnungsnummer" die Nummer der Originalrechnung.
    """
    #: Eine im Verwendungskontext eindeutige Nummer für die Rechnung
    rechnungsnummer: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Ausstellungsdatum der Rechnung
    rechnungsdatum: datetime = attrs.field(validator=attrs.validators.instance_of(datetime))
    #: Zu diesem Datum ist die Zahlung fällig
    faelligkeitsdatum: datetime = attrs.field(validator=attrs.validators.instance_of(datetime))
    #: Ein kontextbezogender Rechnungstyp, z.B. Netznutzungsrechnung
    rechnungstyp: Rechnungstyp = attrs.field(validator=attrs.validators.instance_of(Rechnungstyp))
    #: Der Zeitraum der zugrunde liegenden Lieferung zur Rechnung
    rechnungsperiode: Zeitraum = attrs.field(validator=attrs.validators.instance_of(Zeitraum))
    #: Der Aussteller der Rechnung
    rechnungsersteller: Geschaeftspartner = attrs.field(validator=attrs.validators.instance_of(Geschaeftspartner))
    #: Der Aussteller der Rechnung
    rechnungsempfaenger: Geschaeftspartner = attrs.field(validator=attrs.validators.instance_of(Geschaeftspartner))
    #: Die Summe der Nettobeträge der Rechnungsteile
    gesamtnetto: Betrag = attrs.field(validator=attrs.validators.instance_of(Betrag))
    #: Die Summe der Steuerbeträge der Rechnungsteile
    gesamtsteuer: Betrag = attrs.field(validator=attrs.validators.instance_of(Betrag))
    #: Die Summe aus Netto- und Steuerbetrag
    gesamtbrutto: Betrag = attrs.field(validator=attrs.validators.instance_of(Betrag))
    #: Der zu zahlende Betrag, der sich aus (gesamtbrutto - vorausbezahlt - rabattBrutto) ergibt
    zuzahlen: Betrag = attrs.field(validator=attrs.validators.instance_of(Betrag))
    #: Die Rechnungspositionen
    rechnungspositionen: List[Rechnungsposition] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Rechnungsposition),
            iterable_validator=attrs.validators.instance_of(List),
        )
    )

    # optional attributes
    #: Bezeichnung für die vorliegende Rechnung
    rechnungstitel: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Status der Rechnung zur Kennzeichnung des Bearbeitungsstandes
    rechnungsstatus: Optional[Rechnungsstatus] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Rechnungsstatus))
    )
    #: Im Falle einer Stornorechnung (storno = true) steht hier die Rechnungsnummer der stornierten Rechnung
    original_rechnungsnummer: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Die Summe evtl. vorausgezahlter Beträge, z.B. Abschläge. Angabe als Bruttowert
    vorausgezahlt: Optional[Betrag] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Betrag))
    )
    #: Gesamtrabatt auf den Bruttobetrag
    rabatt_brutto: Optional[Betrag] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Betrag))
    )
    steuerbetraege: Optional[List[Steuerbetrag]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Steuerbetrag),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )
    """
    Eine Liste mit Steuerbeträgen pro Steuerkennzeichen/Steuersatz;
    die Summe dieser Beträge ergibt den Wert für gesamtsteuer.
    """


class RechnungSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Rechnung
    """

    class_name = Rechnung  # type:ignore[assignment]

    # required attributes
    storno = fields.Bool()
    rechnungsnummer = fields.Str()
    rechnungsdatum = fields.DateTime()
    faelligkeitsdatum = fields.DateTime()
    rechnungstyp = EnumField(Rechnungstyp)
    rechnungsperiode = fields.Nested(ZeitraumSchema)
    rechnungsersteller = fields.Nested(GeschaeftspartnerSchema)
    rechnungsempfaenger = fields.Nested(GeschaeftspartnerSchema)
    gesamtnetto = fields.Nested(BetragSchema)
    gesamtsteuer = fields.Nested(BetragSchema)
    gesamtbrutto = fields.Nested(BetragSchema)
    zuzahlen = fields.Nested(BetragSchema)
    rechnungspositionen = fields.List(fields.Nested(RechnungspositionSchema))

    # optional attributes
    rechnungstitel = fields.Str(allow_none=True)
    rechnungsstatus = EnumField(Rechnungsstatus, allow_none=True)
    original_rechnungsnummer = fields.Str(allow_none=True, data_key="originalRechnungsnummer")
    vorausgezahlt = fields.Nested(BetragSchema, allow_none=True)
    rabatt_brutto = fields.Nested(BetragSchema, allow_none=True, data_key="rabattBrutto")
    steuerbetraege = fields.List(fields.Nested(SteuerbetragSchema), allow_none=True)
