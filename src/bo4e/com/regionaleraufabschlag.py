"""
Contains RegionalerAufAbschlag class and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.energiemix import Energiemix, EnergiemixSchema
from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel, RegionalePreisstaffelSchema
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung, TarifeinschraenkungSchema
from bo4e.com.vertragskonditionen import Vertragskonditionen, VertragskonditionenSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class RegionalerAufAbschlag(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten
    abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert, die sich durch die Auswahl eines Auf-
    oder Abschlags ergeben.

    .. HINT::
        `RegionalerAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalerAufAbschlagSchema.json>`_

    """

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))

    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    staffeln: List[RegionalePreisstaffel] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(RegionalePreisstaffel),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Beschreibung des Auf-/Abschlags
    beschreibung: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )

    #: Typ des Aufabschlages (z.B. absolut oder prozentual)
    auf_abschlagstyp: Optional[AufAbschlagstyp] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(AufAbschlagstyp)), default=None
    )

    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.
    auf_abschlagsziel: Optional[AufAbschlagsziel] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(AufAbschlagsziel)), default=None
    )

    #: Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird (nur im Falle absoluter Aufschlagstypen).
    einheit: Optional[Waehrungseinheit] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Waehrungseinheit)), default=None
    )

    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind
    website: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )

    #: Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhältlich sind
    zusatzprodukte: Optional[List[str]] = attrs.field(
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(str),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
        default=None,
    )

    #: Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann
    voraussetzungen: Optional[List[str]] = attrs.field(
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(str),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
        default=None,
    )

    #: Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten
    tarifnamensaenderungen: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )

    #: Zeitraum, in dem der Abschlag zur Anwendung kommen kann
    gueltigkeitszeitraum: Optional[Zeitraum] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum)), default=None
    )

    energiemixaenderung: Optional[Energiemix] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Energiemix)), default=None
    )
    """
    Der Energiemix kann sich durch einen AufAbschlag ändern (z.B. zwei Cent Aufschlag für Ökostrom).
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben.
    """

    vertagskonditionsaenderung: Optional[Vertragskonditionen] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Vertragskonditionen)), default=None
    )
    """
    Änderungen in den Vertragskonditionen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """

    garantieaenderung: Optional[Preisgarantie] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Preisgarantie)), default=None
    )
    """
    Änderungen in den Garantievereinbarungen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """

    einschraenkungsaenderung: Optional[Tarifeinschraenkung] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Tarifeinschraenkung)), default=None
    )
    """
    Änderungen in den Einschränkungen zum Tarif;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """


class RegionalerAufAbschlagSchema(COMSchema):
    """
    Schema for de-/serialization of RegionalerAufAbschlag
    """

    class_name = RegionalerAufAbschlag
    # required attributes
    bezeichnung = fields.Str()
    staffeln = fields.List(fields.Nested(RegionalePreisstaffelSchema))

    # optional attributes
    beschreibung = fields.Str(default=None)
    auf_abschlagstyp = EnumField(AufAbschlagstyp, default=None, data_key="aufAbschlagstyp")
    auf_abschlagsziel = EnumField(AufAbschlagsziel, default=None, data_key="aufAbschlagsziel")
    einheit = EnumField(Waehrungseinheit, default=None)
    website = fields.Str(default=None)
    zusatzprodukte = fields.List(fields.Str(), default=None)
    voraussetzungen = fields.List(fields.Str(), default=None)

    tarifnamensaenderungen = fields.Str(default=None)
    gueltigkeitszeitraum = fields.Nested(ZeitraumSchema, default=None)
    energiemixaenderung = fields.Nested(EnergiemixSchema, default=None)
    vertagskonditionsaenderung = fields.Nested(VertragskonditionenSchema, default=None)
    garantieaenderung = fields.Nested(PreisgarantieSchema, default=None)
    einschraenkungsaenderung = fields.Nested(TarifeinschraenkungSchema, default=None)
