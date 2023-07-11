"""
Contains Ausschreibungslos class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.com.ausschreibungsdetail import Ausschreibungsdetail
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.preismodell import Preismodell
from bo4e.enum.rechnungslegung import Rechnungslegung
from bo4e.enum.sparte import Sparte
from bo4e.enum.vertragsform import Vertragsform


class Ausschreibungslos(COM):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungslos.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungslos JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Ausschreibungslos.json>`_

    """

    # required attributes
    #: Laufende Nummer des Loses
    losnummer: str
    #: Bezeichnung der Ausschreibung
    bezeichnung: str
    #: Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung
    preismodell: Preismodell

    #: Unterscheidungsmöglichkeiten für die Sparte
    energieart: Sparte
    #: Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen
    wunsch_rechnungslegung: Rechnungslegung
    #: Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen
    wunsch_vertragsform: Vertragsform
    #: Name des Lizenzpartners
    betreut_durch: str
    #: Anzahl der Lieferstellen in dieser Ausschreibung
    anzahl_lieferstellen: int

    #: Die ausgeschriebenen Lieferstellen
    lieferstellen: Annotated[list[Ausschreibungsdetail], Len(1)]

    #: Zeitraum, für den die in diesem Los enthaltenen Lieferstellen beliefert werden sollen
    lieferzeitraum: Zeitraum

    # optional attributes
    #: Bemerkung des Kunden zum Los
    bemerkung: Optional[str] = None
    #: Gibt den Gesamtjahresverbrauch (z.B. in kWh) aller in diesem Los enthaltenen Lieferstellen an
    gesamt_menge: Optional[Menge] = None
    #: Mindesmenge Toleranzband (kWh, %)
    wunsch_mindestmenge: Optional[Menge] = None
    #: Maximalmenge Toleranzband (kWh, %)
    wunsch_maximalmenge: Optional[Menge] = None

    wiederholungsintervall: Optional[Zeitraum] = None
    """
    In welchem Intervall die Angebotsabgabe wiederholt werden darf.
    Angabe nur gesetzt für die 2. Phase bei öffentlich-rechtlichen Ausschreibungen
    """

    #: Kundenwunsch zur Kündigungsfrist in der Ausschreibung
    wunsch_kuendingungsfrist: Optional[Zeitraum] = None
    #: Kundenwunsch zum Zahlungsziel in der Ausschreibung
    wunsch_zahlungsziel: Optional[Zeitraum] = None
