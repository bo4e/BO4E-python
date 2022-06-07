"""
Contains AufAbschlagRegional and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.aufabschlagproort import AufAbschlagProOrt, AufAbschlagProOrtSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.energiemix import Energiemix, EnergiemixSchema
from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung, TarifeinschraenkungSchema
from bo4e.com.vertragskonditionen import Vertragskonditionen, VertragskonditionenSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class AufAbschlagRegional(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen
    im Zusammenhang mit regionalen Gültigkeiten abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert,
    die sich durch die Auswahl eines Auf- oder Abschlags ergeben.

    .. HINT::
        `AufAbschlagRegional JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagRegionalSchema.json>`_

    """

    # required attributess
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    betraege: List[AufAbschlagProOrt] = attrs.field(
        validator=[
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(AufAbschlagProOrt),
                iterable_validator=attrs.validators.instance_of(list),
            ),
            check_list_length_at_least_one,
        ]
    )

    # optional attributes
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #:Typ des Aufabschlages (z.B. absolut oder prozentual)
    auf_abschlagstyp: Optional[AufAbschlagstyp] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(AufAbschlagstyp))
    )
    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.
    auf_abschlagsziel: Optional[AufAbschlagsziel] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(AufAbschlagsziel))
    )
    #: Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct.
    einheit: Optional[Waehrungseinheit] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Waehrungseinheit))
    )
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind
    website: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhältlich sind
    zusatzprodukte: Optional[List[str]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(str),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )
    #: Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann
    voraussetzungen: Optional[List[str]] = attrs.field(
        default=None,
        validator=attrs.validators.optional(
            attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(str),
                iterable_validator=attrs.validators.instance_of(list),
            )
        ),
    )
    #: Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten.
    tarifnamensaenderungen: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Zeitraum, in dem der Abschlag zur Anwendung kommen kann
    gueltigkeitszeitraum: Optional[Zeitraum] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum))
    )
    energiemixaenderung: Optional[Energiemix] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Energiemix))
    )
    """ Der Energiemix kann sich durch einen AufAbschlag ändern (z.B. zwei Cent Aufschlag für Ökostrom:
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben."""
    vertagskonditionsaenderung: Optional[Vertragskonditionen] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Vertragskonditionen))
    )
    """ Änderungen in den Vertragskonditionen. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben."""
    garantieaenderung: Optional[Preisgarantie] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Preisgarantie))
    )
    """ Änderungen in den Garantievereinbarungen. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben."""
    einschraenkungsaenderung: Optional[Tarifeinschraenkung] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Tarifeinschraenkung))
    )
    """ Änderungen in den Einschränkungen zum Tarif. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben."""


class AufAbschlagRegionalSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlagRegional.
    """

    class_name = AufAbschlagRegional
    # required attributes
    bezeichnung = fields.Str()
    betraege = fields.List(fields.Nested(AufAbschlagProOrtSchema))

    # optional attributes
    beschreibung = fields.Str(load_default=None)
    auf_abschlagstyp = EnumField(AufAbschlagstyp, load_default=None, data_key="aufAbschlagstyp")
    auf_abschlagsziel = EnumField(AufAbschlagsziel, load_default=None, data_key="aufAbschlagsziel")
    einheit = EnumField(Waehrungseinheit, load_default=None)
    website = fields.Str(load_default=None)
    zusatzprodukte = fields.List(fields.Str, load_default=None)
    voraussetzungen = fields.List(fields.Str, load_default=None)
    tarifnamensaenderungen = fields.Str(load_default=None)
    gueltigkeitszeitraum = fields.Nested(ZeitraumSchema, load_default=None)
    energiemixaenderung = fields.Nested(EnergiemixSchema, load_default=None)
    vertagskonditionsaenderung = fields.Nested(VertragskonditionenSchema, load_default=None)
    garantieaenderung = fields.Nested(PreisgarantieSchema, load_default=None)
    einschraenkungsaenderung = fields.Nested(TarifeinschraenkungSchema, load_default=None)
