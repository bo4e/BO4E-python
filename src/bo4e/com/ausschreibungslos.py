"""
Contains Ausschreibungslos class and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.ausschreibungsdetail import Ausschreibungsdetail
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.preismodell import Preismodell
from bo4e.enum.rechnungslegung import Rechnungslegung
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsform import Vertragsform
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Ausschreibungslos(COM):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung
    """

    # required attributes
    #: Laufende Nummer des Loses
    losnummer: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Bezeichnung des Loses
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung
    preismodell: Preismodell = attr.ib(validator=attr.validators.instance_of(Preismodell))

    #: Unterscheidungsmöglichkeiten für die Sparte
    energieart: Sparte = attr.ib(validator=attr.validators.instance_of(Sparte))
    #: Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen
    wunsch_rechnungslegung: Rechnungslegung = attr.ib(validator=attr.validators.instance_of(Rechnungslegung))
    #: Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen
    wunsch_vertragsform: Vertragsform = attr.ib(validator=attr.validators.instance_of(Vertragsform))
    #: Name des Lizenzpartners
    betreut_durch: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Anzahl der Lieferstellen in dieser Ausschreibung
    anzahl_lieferstellen: int = attr.ib(validator=attr.validators.instance_of(int))

    #:Die ausgeschriebenen Lieferstellen
    lieferstellen: List[Ausschreibungsdetail] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Ausschreibungsdetail),
            iterable_validator=check_list_length_at_least_one,
        )
    )

    # optional attributes
    #: Bemerkung des Kunden zum Los
    bemerkung: Optional[str] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(str)), default=None
    )
    #: Gibt den Gesamtjahresverbrauch (z.B. in kWh) aller in diesem Los enthaltenen Lieferstellen an
    gesamt_menge: Optional[Menge] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Menge)), default=None
    )
    #: Mindesmenge Toleranzband (kWh, %)
    wunsch_mindestmenge: Optional[Menge] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Menge)), default=None
    )
    #: Maximalmenge Toleranzband (kWh, %)
    wunsch_maximalmenge: Optional[Menge] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Menge)), default=None
    )

    wiederholungsintervall: Optional[Zeitraum] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Zeitraum)), default=None
    )
    """
    In welchem Intervall die Angebotsabgabe wiederholt werden darf.
    Angabe nur gesetzt für die 2. Phase bei öffentlich-rechtlichen Ausschreibungen
    """

    #: Zeitraum, für den die in diesem Los enthaltenen Lieferstellen beliefert werden sollen
    lieferzeitraum: Optional[Zeitraum] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Zeitraum)), default=None
    )
    #: Kundenwunsch zur Kündigungsfrist in der Ausschreibung
    wunsch_kuendingungsfrist: Optional[Zeitraum] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Zeitraum)), default=None
    )
    #: Kundenwunsch zum Zahlungsziel in der Ausschreibung
    wunsch_zahlungsziel: Optional[Zeitraum] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Zeitraum)), default=None
    )


class AusschreibungslosSchema(COMSchema):
    """
    Schema for de-/serialization of Ausschreibungslos.
    """

    # required attributes
    losnummer = fields.String()
    bezeichnung = fields.String()
    preismodell = EnumField(Preismodell)
    energieart = EnumField(Sparte)
    wunsch_rechnungslegung = EnumField(Rechnungslegung)
    wunsch_vertragsform = EnumField(Vertragsform)
    betreut_durch = fields.String()
    anzahl_lieferstellen = fields.Integer()

    # optional attributes
    bemerkung = fields.String(load_default=None)
    gesamt_menge = fields.Nested(MengeSchema, load_default=None)
    wunsch_mindestmenge = fields.Nested(MengeSchema, load_default=None)
    wunsch_maximalmenge = fields.Nested(MengeSchema, load_default=None)
    wiederholungsintervall = fields.Nested(ZeitraumSchema, load_default=None)
    lieferzeitraum = fields.Nested(ZeitraumSchema, load_default=None)
    wunsch_kuendingungsfrist = fields.Nested(ZeitraumSchema, load_default=None)
    wunsch_zahlungsziel = fields.Nested(ZeitraumSchema, load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Ausschreibungslos:
        """Deserialize JSON to Angebotsteil object"""
        return Ausschreibungslos(**data)
