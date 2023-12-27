"""
Contains Ausschreibungslos class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import Optional

from ..enum.preismodell import Preismodell
from ..enum.rechnungslegung import Rechnungslegung
from ..enum.sparte import Sparte
from ..enum.vertragsform import Vertragsform
from ..utils import postprocess_docstring
from .ausschreibungsdetail import Ausschreibungsdetail
from .com import COM
from .menge import Menge
from .zeitraum import Zeitraum


@postprocess_docstring
class Ausschreibungslos(COM):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungslos.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungslos JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Ausschreibungslos.json>`_

    """

    #: Laufende Nummer des Loses
    losnummer: Optional[str] = None
    #: Bezeichnung der Ausschreibung
    bezeichnung: Optional[str] = None
    #: Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung
    preismodell: Optional[Preismodell] = None

    #: Unterscheidungsmöglichkeiten für die Sparte
    energieart: Optional[Sparte] = None
    #: Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen
    wunsch_rechnungslegung: Optional[Rechnungslegung] = None
    #: Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen
    wunsch_vertragsform: Optional[Vertragsform] = None
    #: Name des Lizenzpartners
    betreut_durch: Optional[str] = None
    #: Anzahl der Lieferstellen in dieser Ausschreibung
    anzahl_lieferstellen: Optional[int] = None

    #: Die ausgeschriebenen Lieferstellen
    lieferstellen: Optional[list[Ausschreibungsdetail]] = None

    #: Zeitraum, für den die in diesem Los enthaltenen Lieferstellen beliefert werden sollen
    lieferzeitraum: Optional[Zeitraum] = None

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
