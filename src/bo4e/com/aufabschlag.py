"""
Contains AufAbschlag class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import einheit_only_for_abschlagstyp_absolut


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class AufAbschlag(COM):
    """
    Modell für die preiserhöhenden (Aufschlag) bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen wurden.
    """

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Werte für die gestaffelten Auf/Abschläge.
    staffeln: List[Preisstaffel] = attr.ib(validator=attr.validators.instance_of(List))

    # optional attributes
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )
    #: Typ des Aufabschlages (z.B. absolut oder prozentual).
    auf_abschlagstyp: Optional[AufAbschlagstyp] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(AufAbschlagstyp))
    )
    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc..
    auf_abschlagsziel: Optional[AufAbschlagsziel] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(AufAbschlagsziel))
    )
    einheit: Optional[Waehrungseinheit] = attr.ib(
        default=None,
        validator=[
            attr.validators.optional(attr.validators.instance_of(Waehrungseinheit)),
            einheit_only_for_abschlagstyp_absolut,
        ],
    )
    """ Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct..
    (Nur im Falle absoluter Aufschlagstypen). """
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    website: Optional[str] = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(str)))
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    gueltigkeitszeitraum: Optional[Zeitraum] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Zeitraum))
    )


class AufAbschlagSchema(COMSchema):
    """
    Schema for de-/serialization of AufAbschlag.
    """

    # required attributes
    bezeichnung = fields.Str()
    staffeln = fields.List(fields.Nested(PreisstaffelSchema))

    # optional attributes
    beschreibung = fields.Str(load_default=None)
    auf_abschlagstyp = EnumField(AufAbschlagstyp, allow_none=True)
    auf_abschlagsziel = EnumField(AufAbschlagsziel, allow_none=True)
    einheit = EnumField(Waehrungseinheit, allow_none=True)
    website = fields.Str(load_default=None)
    gueltigkeitszeitraum = fields.Nested(ZeitraumSchema, load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> AufAbschlag:
        """Deserialize JSON to AufAbschlag object"""
        return AufAbschlag(**data)
