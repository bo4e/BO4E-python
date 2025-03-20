"""
Contains RegionalerAufAbschlag class and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

# pylint: disable=R0801
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.aufabschlagstyp import AufAbschlagstyp
    from ..enum.aufabschlagsziel import AufAbschlagsziel
    from ..enum.waehrungseinheit import Waehrungseinheit
    from .energiemix import Energiemix
    from .preisgarantie import Preisgarantie
    from .regionalepreisstaffel import RegionalePreisstaffel
    from .tarifeinschraenkung import Tarifeinschraenkung
    from .vertragskonditionen import Vertragskonditionen
    from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module


@postprocess_docstring
class RegionalerAufAbschlag(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten
    abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert, die sich durch die Auswahl eines Auf-
    oder Abschlags ergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalerAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalerAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RegionalerAufAbschlag.json>`_

    """

    bezeichnung: Optional[str] = None
    """Bezeichnung des Auf-/Abschlags"""

    staffeln: Optional[list["RegionalePreisstaffel"]] = None
    """Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung"""

    beschreibung: Optional[str] = None
    """Beschreibung des Auf-/Abschlags"""

    auf_abschlagstyp: Optional["AufAbschlagstyp"] = None
    """Typ des Aufabschlages (z.B. absolut oder prozentual)"""

    auf_abschlagsziel: Optional["AufAbschlagsziel"] = None
    """Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc."""

    einheit: Optional["Waehrungseinheit"] = None
    """Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird (nur im Falle absoluter Aufschlagstypen)."""

    website: Optional[str] = None
    """Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind"""

    zusatzprodukte: Optional[list[str]] = None
    """Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhältlich sind"""

    voraussetzungen: Optional[list[str]] = None
    """Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann"""

    tarifnamensaenderungen: Optional[str] = None
    """Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten"""

    gueltigkeitszeitraum: Optional["Zeitraum"] = None
    """Zeitraum, in dem der Abschlag zur Anwendung kommen kann"""

    energiemixaenderung: Optional["Energiemix"] = None
    """
    Der Energiemix kann sich durch einen AufAbschlag ändern (z.B. zwei Cent Aufschlag für Ökostrom).
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben.
    """

    vertagskonditionsaenderung: Optional["Vertragskonditionen"] = None
    """
    Änderungen in den Vertragskonditionen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """

    garantieaenderung: Optional["Preisgarantie"] = None
    """
    Änderungen in den Garantievereinbarungen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """

    einschraenkungsaenderung: Optional["Tarifeinschraenkung"] = None
    """
    Änderungen in den Einschränkungen zum Tarif;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """
