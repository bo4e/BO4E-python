"""
Contains class Ausschreibungsdetail and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.zaehlertyp import Zaehlertyp


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Ausschreibungsdetail(COM):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.
    """

    # required attributes
    #: Identifikation einer ausgeschriebenen Marktlokation
    lokations_id: str = attr.ib(validator=attr.validators.instance_of(str))
    #: In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung
    netzebene_lieferung: str = attr.ib(validator=attr.validators.instance_of(Netzebene))
    #: In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung
    netzebene_messung: str = attr.ib(validator=attr.validators.instance_of(Netzebene))
    #: Die Adresse an der die Marktlokation sich befindet
    lokationsadresse: Adresse = attr.ib(validator=attr.validators.instance_of(Adresse))
    #: Angefragter Zeitraum für die ausgeschriebene Belieferung
    lieferzeitraum: Zeitraum = attr.ib(validator=attr.validators.instance_of(Zeitraum))

    # optional attributes
    #: Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'
    netzbetreiber: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)), default=None
    )
    #: Bezeichnung des Kunden, der die Marktlokation nutzt
    kunde: Optional[str] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)), default=None)
    #: Die Bezeichnung des Zählers an der Marktlokation
    zaehlernummer: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)), default=None
    )
    #: Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'
    lokationsbezeichnung: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)), default=None
    )

    #: Spezifikation, um welche Zählertechnik es sich im vorliegenden Fall handelt, z.B. Leistungsmessung
    zaehlertechnik: Optional[Zaehlertyp] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Zaehlertyp)), default=None
    )
    lastgang_vorhanden: Optional[bool] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(bool)), default=None
    )
    """
    Zeigt an, ob es zu der Marktlokation einen Lastgang gibt.
    Falls ja, kann dieser abgerufen werden und daraus die Verbrauchswerte ermittelt werden
    """

    #: Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    prognose_jahresarbeit: Optional[Menge] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Menge)), default=None
    )
    #: Ein Prognosewert für die Arbeit innerhalb des angefragten Lieferzeitraums der ausgeschriebenen Lokation
    prognose_arbeit_lieferzeitraum: Optional[Menge] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Menge)), default=None
    )
    #: Prognosewert für die abgenommene maximale Leistung der ausgeschriebenen Lokation
    prognose_leistung: Optional[Menge] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Menge)), default=None
    )
    #: Die (evtl. abweichende) Rechnungsadresse
    rechnungsadresse: Optional[Adresse] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Adresse)), default=None
    )


class AusschreibungsdetailSchema(COMSchema):
    """
    Schema for de-/serialization of Ausschreibungsdetail
    """

    # required attributes
    lokations_id = fields.Str()
    netzebene_lieferung = EnumField(Netzebene)
    netzebene_messung = EnumField(Netzebene)
    lokationsadresse = fields.Nested(AdresseSchema)
    lieferzeitraum = fields.Nested(ZeitraumSchema)

    # optional attributes
    netzbetreiber = fields.Str(allow_none=True)
    kunde = fields.Str(allow_none=True)
    zaehlernummer = fields.Str(allow_none=True)
    lokationsbezeichnung = fields.Str(allow_none=True)
    zaehlertechnik = EnumField(Zaehlertyp, allow_none=True)
    lastgang_vorhanden = fields.Boolean(allow_none=True)
    prognose_jahresarbeit = fields.Nested(MengeSchema, allow_none=True)
    prognose_arbeit_lieferzeitraum = fields.Nested(MengeSchema, allow_none=True)
    prognose_leistung = fields.Nested(MengeSchema, allow_none=True)
    rechnungsadresse = fields.Nested(AdresseSchema, allow_none=True)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Ausschreibungsdetail:
        """Deserialize JSON to Ausschreibungsdetail object"""
        return Ausschreibungsdetail(**data)
