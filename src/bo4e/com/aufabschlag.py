"""
Contains AufAbschlag class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import einheit_only_for_abschlagstyp_absolut


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class AufAbschlag(COM):
    """
    Modell für die preiserhöhenden (Aufschlag) bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen wurden.

    .. HINT::
        `AufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagSchema.json>`_

    """

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Werte für die gestaffelten Auf/Abschläge.
    staffeln: List[Preisstaffel] = attrs.field(validator=attrs.validators.instance_of(List))

    # optional attributes
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Typ des Aufabschlages (z.B. absolut oder prozentual).
    auf_abschlagstyp: Optional[AufAbschlagstyp] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(AufAbschlagstyp))
    )
    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc..
    auf_abschlagsziel: Optional[AufAbschlagsziel] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(AufAbschlagsziel))
    )
    einheit: Optional[Waehrungseinheit] = attrs.field(
        default=None,
        validator=[
            attrs.validators.optional(attrs.validators.instance_of(Waehrungseinheit)),
            einheit_only_for_abschlagstyp_absolut,
        ],
    )
    """ Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct..
    (Nur im Falle absoluter Aufschlagstypen). """
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    website: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    gueltigkeitszeitraum: Optional[Zeitraum] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum))
    )


class AufAbschlagSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlag
    """

    class_name = AufAbschlag
    # required attributes
    bezeichnung = fields.Str()
    staffeln = fields.List(fields.Nested(PreisstaffelSchema))

    # optional attributes
    beschreibung = fields.Str(load_default=None)
    auf_abschlagstyp = EnumField(AufAbschlagstyp, allow_none=True, data_key="aufAbschlagstyp")
    auf_abschlagsziel = EnumField(AufAbschlagsziel, allow_none=True, data_key="aufAbschlagsziel")
    einheit = EnumField(Waehrungseinheit, allow_none=True)
    website = fields.Str(load_default=None)
    gueltigkeitszeitraum = fields.Nested(ZeitraumSchema, load_default=None)
