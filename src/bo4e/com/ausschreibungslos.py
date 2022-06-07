"""
Contains Ausschreibungslos class and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.ausschreibungsdetail import Ausschreibungsdetail, AusschreibungsdetailSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.preismodell import Preismodell
from bo4e.enum.rechnungslegung import Rechnungslegung
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsform import Vertragsform
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Ausschreibungslos(COM):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung

    .. HINT::
        `Ausschreibungslos JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AusschreibungslosSchema.json>`_

    """

    # required attributes
    #: Laufende Nummer des Loses
    losnummer: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Bezeichnung der Ausschreibung
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung
    preismodell: Preismodell = attrs.field(validator=attrs.validators.instance_of(Preismodell))

    #: Unterscheidungsmöglichkeiten für die Sparte
    energieart: Sparte = attrs.field(validator=attrs.validators.instance_of(Sparte))
    #: Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen
    wunsch_rechnungslegung: Rechnungslegung = attrs.field(validator=attrs.validators.instance_of(Rechnungslegung))
    #: Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen
    wunsch_vertragsform: Vertragsform = attrs.field(validator=attrs.validators.instance_of(Vertragsform))
    #: Name des Lizenzpartners
    betreut_durch: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Anzahl der Lieferstellen in dieser Ausschreibung
    anzahl_lieferstellen: int = attrs.field(validator=attrs.validators.instance_of(int))

    #: Die ausgeschriebenen Lieferstellen
    lieferstellen: List[Ausschreibungsdetail] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Ausschreibungsdetail),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    #: Zeitraum, für den die in diesem Los enthaltenen Lieferstellen beliefert werden sollen
    lieferzeitraum: Zeitraum = attrs.field(validator=attrs.validators.instance_of(Zeitraum))

    # optional attributes
    #: Bemerkung des Kunden zum Los
    bemerkung: Optional[str] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(str)), default=None
    )
    #: Gibt den Gesamtjahresverbrauch (z.B. in kWh) aller in diesem Los enthaltenen Lieferstellen an
    gesamt_menge: Optional[Menge] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Menge)), default=None
    )
    #: Mindesmenge Toleranzband (kWh, %)
    wunsch_mindestmenge: Optional[Menge] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Menge)), default=None
    )
    #: Maximalmenge Toleranzband (kWh, %)
    wunsch_maximalmenge: Optional[Menge] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Menge)), default=None
    )

    wiederholungsintervall: Optional[Zeitraum] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum)), default=None
    )
    """
    In welchem Intervall die Angebotsabgabe wiederholt werden darf.
    Angabe nur gesetzt für die 2. Phase bei öffentlich-rechtlichen Ausschreibungen
    """

    #: Kundenwunsch zur Kündigungsfrist in der Ausschreibung
    wunsch_kuendingungsfrist: Optional[Zeitraum] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum)), default=None
    )
    #: Kundenwunsch zum Zahlungsziel in der Ausschreibung
    wunsch_zahlungsziel: Optional[Zeitraum] = attrs.field(
        validator=attrs.validators.optional(attrs.validators.instance_of(Zeitraum)), default=None
    )


class AusschreibungslosSchema(COMSchema):
    """
    Schema for de-/serialization of Ausschreibungslos.
    """

    class_name = Ausschreibungslos

    # required attributes
    losnummer = fields.String()
    bezeichnung = fields.String()
    preismodell = EnumField(Preismodell)
    energieart = EnumField(Sparte)
    wunsch_rechnungslegung = EnumField(Rechnungslegung, data_key="wunschRechnungslegung")
    wunsch_vertragsform = EnumField(Vertragsform, data_key="wunschVertragsform")
    betreut_durch = fields.String(data_key="betreutDurch")
    anzahl_lieferstellen = fields.Integer(data_key="anzahlLieferstellen")
    lieferstellen = fields.List(fields.Nested(AusschreibungsdetailSchema))
    lieferzeitraum = fields.Nested(ZeitraumSchema)

    # optional attributes
    bemerkung = fields.String(load_default=None)
    gesamt_menge = fields.Nested(MengeSchema, load_default=None, data_key="gesamtMenge")
    wunsch_mindestmenge = fields.Nested(MengeSchema, load_default=None, data_key="wunschMindestmenge")
    wunsch_maximalmenge = fields.Nested(MengeSchema, load_default=None, data_key="wunschMaximalmenge")
    wiederholungsintervall = fields.Nested(ZeitraumSchema, load_default=None)
    wunsch_kuendingungsfrist = fields.Nested(ZeitraumSchema, load_default=None, data_key="wunschKuendingungsfrist")
    wunsch_zahlungsziel = fields.Nested(ZeitraumSchema, load_default=None, data_key="wunschZahlungsziel")
