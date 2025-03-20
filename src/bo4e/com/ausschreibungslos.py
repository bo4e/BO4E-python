"""
Contains Ausschreibungslos class and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.preismodell import Preismodell
    from ..enum.rechnungslegung import Rechnungslegung
    from ..enum.sparte import Sparte
    from ..enum.vertragsform import Vertragsform
    from .ausschreibungsdetail import Ausschreibungsdetail
    from .menge import Menge
    from .zeitraum import Zeitraum


@postprocess_docstring
class Ausschreibungslos(COM):
    """
    Eine Komponente zur Abbildung einzelner Lose einer Ausschreibung

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungslos.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungslos JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Ausschreibungslos.json>`_

    """

    losnummer: Optional[str] = None
    """Laufende Nummer des Loses"""
    bezeichnung: Optional[str] = None
    """Bezeichnung der Ausschreibung"""
    preismodell: Optional["Preismodell"] = None
    """Bezeichnung der Preismodelle in Ausschreibungen für die Energielieferung"""

    energieart: Optional["Sparte"] = None
    """Unterscheidungsmöglichkeiten für die Sparte"""
    wunsch_rechnungslegung: Optional["Rechnungslegung"] = None
    """Aufzählung der Möglichkeiten zur Rechnungslegung in Ausschreibungen"""
    wunsch_vertragsform: Optional["Vertragsform"] = None
    """Aufzählung der Möglichkeiten zu Vertragsformen in Ausschreibungen"""
    betreut_durch: Optional[str] = None
    """Name des Lizenzpartners"""
    anzahl_lieferstellen: Optional[int] = None
    """Anzahl der Lieferstellen in dieser Ausschreibung"""

    lieferstellen: Optional[list["Ausschreibungsdetail"]] = None
    """Die ausgeschriebenen Lieferstellen"""

    lieferzeitraum: Optional["Zeitraum"] = None
    """Zeitraum, für den die in diesem Los enthaltenen Lieferstellen beliefert werden sollen"""

    bemerkung: Optional[str] = None
    """Bemerkung des Kunden zum Los"""
    gesamt_menge: Optional["Menge"] = None
    """Gibt den Gesamtjahresverbrauch (z.B. in kWh) aller in diesem Los enthaltenen Lieferstellen an"""
    wunsch_mindestmenge: Optional["Menge"] = None
    """Mindesmenge Toleranzband (kWh, %)"""
    wunsch_maximalmenge: Optional["Menge"] = None
    """Maximalmenge Toleranzband (kWh, %)"""

    wiederholungsintervall: Optional["Zeitraum"] = None
    """
    In welchem Intervall die Angebotsabgabe wiederholt werden darf.
    Angabe nur gesetzt für die 2. Phase bei öffentlich-rechtlichen Ausschreibungen
    """

    wunsch_kuendingungsfrist: Optional["Zeitraum"] = None
    """Kundenwunsch zur Kündigungsfrist in der Ausschreibung"""
    wunsch_zahlungsziel: Optional["Zeitraum"] = None
    """Kundenwunsch zum Zahlungsziel in der Ausschreibung"""
