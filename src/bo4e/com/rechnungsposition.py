"""
Contains Rechnungsposition class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.preis import Preis, PreisSchema
from bo4e.com.steuerbetrag import Steuerbetrag, SteuerbetragSchema
from bo4e.enum.artikelid import ArtikelId
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.zeiteinheit import Zeiteinheit
from bo4e.validators import check_bis_is_later_than_von, validate_marktlokations_id


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Rechnungsposition(COM):
    """
    Über Rechnungspositionen werden Rechnungen strukturiert.
    In einem Rechnungsteil wird jeweils eine in sich geschlossene Leistung abgerechnet.

    .. HINT::
        `Rechnungsposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RechnungspositionSchema.json>`_

    """

    # required attributes
    #: Fortlaufende Nummer für die Rechnungsposition
    positionsnummer: int = attrs.field(validator=attrs.validators.instance_of(int))

    lieferung_von: datetime = attrs.field(
        validator=[attrs.validators.instance_of(datetime), check_bis_is_later_than_von]
    )  #: Start der Lieferung für die abgerechnete Leistung (inklusiv)
    lieferung_bis: datetime = attrs.field(
        validator=[attrs.validators.instance_of(datetime), check_bis_is_later_than_von]
    )  #: Ende der Lieferung für die abgerechnete Leistung (exklusiv)

    #: Bezeichung für die abgerechnete Position
    positionstext: str = attrs.field(validator=attrs.validators.instance_of(str))

    #: Die abgerechnete Menge mit Einheit
    positions_menge: Menge = attrs.field(validator=attrs.validators.instance_of(Menge))
    #: Der Preis für eine Einheit der energetischen Menge
    einzelpreis: Preis = attrs.field(validator=attrs.validators.instance_of(Preis))

    teilsumme_netto: Betrag = attrs.field(validator=attrs.validators.instance_of(Betrag))
    """
    Das Ergebnis der Multiplikation aus einzelpreis * positionsMenge * (Faktor aus zeitbezogeneMenge).
    Z.B. 12,60€ * 120 kW * 3/12 (für 3 Monate).
    """
    # the cross check in general doesn't work because Betrag and Preis use different enums to describe the currency
    # see https://github.com/Hochfrequenz/BO4E-python/issues/126

    #: Auf die Position entfallende Steuer, bestehend aus Steuersatz und Betrag
    teilsumme_steuer: Steuerbetrag = attrs.field(validator=attrs.validators.instance_of(Steuerbetrag))

    # optional attributes
    #: Falls sich der Preis auf eine Zeit bezieht, steht hier die Einheit
    zeiteinheit: Optional[Zeiteinheit] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Zeiteinheit))
    )

    #: Kennzeichnung der Rechnungsposition mit der Standard-Artikelnummer des BDEW
    artikelnummer: Optional[BDEWArtikelnummer] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(BDEWArtikelnummer))
    )
    #: Marktlokation, die zu dieser Position gehört
    lokations_id: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(validate_marktlokations_id)
    )

    zeitbezogene_menge: Optional[Menge] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Menge))
    )
    """
    Eine auf die Zeiteinheit bezogene Untermenge.
    Z.B. bei einem Jahrespreis, 3 Monate oder 146 Tage.
    Basierend darauf wird der Preis aufgeteilt.
    """
    #: Nettobetrag für den Rabatt dieser Position
    teilrabatt_netto: Optional[Betrag] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Betrag))
    )

    artikel_id: Optional[ArtikelId] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(ArtikelId)), default=None
    )  #: Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst

    def _get_inclusive_start(self) -> datetime:
        """return the inclusive start (used in the validator)"""
        return self.lieferung_von

    def _get_exclusive_end(self) -> datetime:
        """return the exclusive end (used in the validator)"""
        return self.lieferung_bis


class RechnungspositionSchema(COMSchema):
    """
    Schema for de-/serialization of RechnungspositionSchema
    """

    class_name = Rechnungsposition

    # required attributes
    positionsnummer = fields.Integer()
    lieferung_von = fields.DateTime(data_key="lieferungVon")
    lieferung_bis = fields.DateTime(data_key="lieferungBis")
    positionstext = fields.String()
    positions_menge = fields.Nested(MengeSchema, data_key="positionsMenge")
    einzelpreis = fields.Nested(PreisSchema)
    teilsumme_netto = fields.Nested(BetragSchema, data_key="teilsummeNetto")
    teilsumme_steuer = fields.Nested(SteuerbetragSchema, data_key="teilsummeSteuer")

    # optional attributes
    zeiteinheit = EnumField(Zeiteinheit, load_default=None)
    artikelnummer = EnumField(BDEWArtikelnummer, load_default=None)
    lokations_id = fields.String(load_default=None, data_key="lokationsId")
    zeitbezogene_menge = fields.Nested(MengeSchema, load_default=None, data_key="zeitbezogeneMenge")
    teilrabatt_netto = fields.Nested(BetragSchema, load_default=None, data_key="teilrabattNetto")
    artikel_id = EnumField(ArtikelId, load_default=None, data_key="artikelId")
