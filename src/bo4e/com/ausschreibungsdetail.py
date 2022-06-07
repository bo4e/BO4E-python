"""
Contains class Ausschreibungsdetail and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.zaehlertyp import Zaehlertyp


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Ausschreibungsdetail(COM):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.

    .. HINT::
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AusschreibungsdetailSchema.json>`_

    """

    # required attributes
    #: Identifikation einer ausgeschriebenen Marktlokation
    lokations_id: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung
    netzebene_lieferung: str = attrs.field(validator=attrs.validators.instance_of(Netzebene))
    #: In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung
    netzebene_messung: str = attrs.field(validator=attrs.validators.instance_of(Netzebene))
    #: Die Adresse an der die Marktlokation sich befindet
    lokationsadresse: Adresse = attrs.field(validator=attrs.validators.instance_of(Adresse))
    #: Angefragter Zeitraum für die ausgeschriebene Belieferung
    lieferzeitraum: Zeitraum = attrs.field(validator=attrs.validators.instance_of(Zeitraum))

    # optional attributes
    #: Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'
    netzbetreiber: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )
    #: Bezeichnung des Kunden, der die Marktlokation nutzt
    kunde: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )
    #: Die Bezeichnung des Zählers an der Marktlokation
    zaehlernummer: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )
    #: Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'
    lokationsbezeichnung: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )

    #: Spezifikation, um welche Zählertechnik es sich im vorliegenden Fall handelt, z.B. Leistungsmessung
    zaehlertechnik: Optional[Zaehlertyp] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Zaehlertyp)), default=None
    )
    lastgang_vorhanden: Optional[bool] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(bool)), default=None
    )
    """
    Zeigt an, ob es zu der Marktlokation einen Lastgang gibt.
    Falls ja, kann dieser abgerufen werden und daraus die Verbrauchswerte ermittelt werden
    """

    #: Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    prognose_jahresarbeit: Optional[Menge] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Menge)), default=None
    )
    #: Ein Prognosewert für die Arbeit innerhalb des angefragten Lieferzeitraums der ausgeschriebenen Lokation
    prognose_arbeit_lieferzeitraum: Optional[Menge] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Menge)), default=None
    )
    #: Prognosewert für die abgenommene maximale Leistung der ausgeschriebenen Lokation
    prognose_leistung: Optional[Menge] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Menge)), default=None
    )
    #: Die (evtl. abweichende) Rechnungsadresse
    rechnungsadresse: Optional[Adresse] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Adresse)), default=None
    )


class AusschreibungsdetailSchema(COMSchema):
    """
    Schema for de-/serialization of Ausschreibungsdetail
    """

    class_name = Ausschreibungsdetail
    # required attributes
    lokations_id = fields.Str(data_key="lokationsId")
    netzebene_lieferung = EnumField(Netzebene, data_key="netzebeneLieferung")
    netzebene_messung = EnumField(Netzebene, data_key="netzebeneMessung")
    lokationsadresse = fields.Nested(AdresseSchema)
    lieferzeitraum = fields.Nested(ZeitraumSchema)

    # optional attributes
    netzbetreiber = fields.Str(allow_none=True)
    kunde = fields.Str(allow_none=True)
    zaehlernummer = fields.Str(allow_none=True)
    lokationsbezeichnung = fields.Str(allow_none=True)
    zaehlertechnik = EnumField(Zaehlertyp, allow_none=True)
    lastgang_vorhanden = fields.Boolean(allow_none=True, data_key="lastgangVorhanden")
    prognose_jahresarbeit = fields.Nested(MengeSchema, allow_none=True, data_key="prognoseJahresarbeit")
    prognose_arbeit_lieferzeitraum = fields.Nested(
        MengeSchema, allow_none=True, data_key="prognoseArbeitLieferzeitraum"
    )
    prognose_leistung = fields.Nested(MengeSchema, allow_none=True, data_key="prognoseLeistung")
    rechnungsadresse = fields.Nested(AdresseSchema, allow_none=True)
