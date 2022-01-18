"""
Contains Preisposition class and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.enum.artikelid import ArtikelId
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.bemessungsgroesse import Bemessungsgroesse
from bo4e.enum.kalkulationsmethode import Kalkulationsmethode
from bo4e.enum.leistungstyp import Leistungstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.tarifzeit import Tarifzeit
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.enum.zeiteinheit import Zeiteinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Preisposition(COM):
    """
    Preis für eine definierte Lieferung oder Leistung innerhalb eines Preisblattes
    """

    # required attributes
    #: Das Modell, das der Preisbildung zugrunde liegt
    berechnungsmethode: Kalkulationsmethode = attr.ib(validator=attr.validators.instance_of(Kalkulationsmethode))
    #: Standardisierte Bezeichnung für die abgerechnete Leistungserbringung
    leistungstyp: Leistungstyp = attr.ib(validator=attr.validators.instance_of(Leistungstyp))  #
    #: Bezeichnung für die in der Position abgebildete Leistungserbringung
    leistungsbezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Festlegung, mit welcher Preiseinheit abgerechnet wird, z.B. Ct. oder €
    preiseinheit: Waehrungseinheit = attr.ib(validator=attr.validators.instance_of(Waehrungseinheit))
    #: Hier wird festgelegt, auf welche Bezugsgrösse sich der Preis bezieht, z.B. kWh oder Stück
    bezugsgroesse: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))
    #: Preisstaffeln, die zu dieser Preisposition gehören
    preisstaffeln: List[Preisstaffel] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Preisstaffel),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    zeitbasis: Optional[Zeiteinheit] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Zeiteinheit))
    )
    """
    Die Zeit(dauer) auf die sich der Preis bezieht.
    Z.B. ein Jahr für einen Leistungspreis der in €/kW/Jahr ausgegeben wird
    """
    #: Festlegung, für welche Tarifzeit der Preis hier festgelegt ist
    tarifzeit: Optional[Tarifzeit] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Tarifzeit))
    )
    bdew_artikelnummer: Optional[BDEWArtikelnummer] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(BDEWArtikelnummer))
    )
    """
    Eine vom BDEW standardisierte Bezeichnug für die abgerechnete Leistungserbringung;
    Diese Artikelnummer wird auch im Rechnungsteil der INVOIC verwendet.
    """
    #: Mit der Menge der hier angegebenen Größe wird die Staffelung/Zonung durchgeführt. Z.B. Vollbenutzungsstunden
    zonungsgroesse: Optional[Bemessungsgroesse] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Bemessungsgroesse))
    )
    #: Der Anteil der Menge der Blindarbeit in Prozent von der Wirkarbeit, für die keine Abrechnung erfolgt
    freimenge_blindarbeit: Optional[Decimal] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Decimal))
    )
    freimenge_leistungsfaktor: Optional[Decimal] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Decimal))
    )
    """
    Der cos phi (Verhältnis Wirkleistung/Scheinleistung) aus dem die Freimenge für die Blindarbeit berechnet wird als
    tan phi (Verhältnis Blindleistung/Wirkleistung)
    """
    artikel_id: Optional[ArtikelId] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(ArtikelId)), default=None
    )  #: Standardisierte vom BDEW herausgegebene Liste, welche im Strommarkt die BDEW-Artikelnummer ablöst


class PreispositionSchema(COMSchema):
    """
    Schema for de-/serialization of Preisposition
    """

    class_name = Preisposition

    # required attributes
    berechnungsmethode = EnumField(Kalkulationsmethode)
    leistungstyp = EnumField(Leistungstyp)
    leistungsbezeichnung = fields.Str()
    preiseinheit = EnumField(Waehrungseinheit)
    bezugsgroesse = EnumField(Mengeneinheit)
    preisstaffeln = fields.List(fields.Nested(PreisstaffelSchema))

    # optional attributes
    zeitbasis = EnumField(Zeiteinheit, load_default=None)
    tarifzeit = EnumField(Tarifzeit, load_default=None)
    bdew_artikelnummer = EnumField(BDEWArtikelnummer, load_default=None)
    zonungsgroesse = EnumField(Bemessungsgroesse, load_default=None)
    freimenge_blindarbeit = fields.Decimal(load_default=None, as_string=True)
    freimenge_leistungsfaktor = fields.Decimal(load_default=None, as_string=True)
    artikel_id = EnumField(ArtikelId, load_default=None)
