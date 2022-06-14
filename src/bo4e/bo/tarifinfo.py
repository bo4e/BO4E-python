"""
Contains Tarifinfo class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.marktteilnehmer import Marktteilnehmer
from bo4e.com.energiemix import Energiemix
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Tarifinfo(Geschaeftsobjekt):
    """
    Das BO Tarifinfo liefert die Merkmale, die einen Endkundentarif identifizierbar machen.
    Dieses BO dient als Basis für weitere BOs mit erweiterten Anwendungsmöglichkeiten.

    .. HINT::
        `Tarifinfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/TarifinfoSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.TARIFINFO
    #: Name des Tarifs
    bezeichnung: str
    #: Der Name des Marktpartners, der den Tarif anbietet
    anbietername: str
    #: Strom oder Gas, etc.
    sparte: Sparte
    #: Kundentypen für den der Tarif gilt, z.B. Privatkunden
    kundentypen: List[Kundentyp] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Kundentyp),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    #: Die Art des Tarifes, z.B. Eintarif oder Mehrtarif
    tarifart: Tarifart
    #: Hinweis auf den Tariftyp, z.B. Grundversorgung oder Sondertarif
    tariftyp: Tariftyp
    #: Weitere Merkmale des Tarifs, z.B. Festpreis oder Vorkasse
    tarifmerkmale: List[Tarifmerkmal] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Tarifmerkmal),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    #: Der Marktteilnehmer (Lieferant), der diesen Tarif anbietet
    anbieter: Marktteilnehmer

    # optional attributes
    #: Internetseite auf dem der Tarif zu finden ist
    website: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Freitext
    bemerkung: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )

    #: Angabe, in welchem Zeitraum der Tarif gültig ist
    zeitliche_gueltigkeit: Optional[Zeitraum] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum))
    )
    #: Der Energiemix, der für diesen Tarif gilt
    energiemix: Optional[Energiemix] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Energiemix))
    )
    #: Mindestlaufzeiten und Kündigungsfristen zusammengefasst
    vertragskonditionen: Optional[Vertragskonditionen] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Vertragskonditionen))
    )


class TarifinfoSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Tarifinfo
    """

    class_name = Tarifinfo

    bezeichnung = fields.Str()
    anbietername = fields.Str()
    sparte = EnumField(Sparte)
    kundentypen = fields.List(EnumField(Kundentyp))
    tarifart = EnumField(Tarifart)
    tariftyp = EnumField(Tariftyp)
    tarifmerkmale = fields.List(EnumField(Tarifmerkmal))
    anbieter = fields.Nested(MarktteilnehmerSchema)

    # optional attributes
    website = fields.Str(load_default=None)
    bemerkung = fields.Str(load_default=None)
    zeitliche_gueltigkeit = fields.Nested(ZeitraumSchema, load_default=None, data_key="zeitlicheGueltigkeit")
    energiemix = fields.Nested(EnergiemixSchema, load_default=None)
    vertragskonditionen = fields.Nested(VertragskonditionenSchema, load_default=None)
