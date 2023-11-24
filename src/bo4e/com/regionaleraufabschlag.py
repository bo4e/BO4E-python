"""
Contains RegionalerAufAbschlag class and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

from ..enum.aufabschlagstyp import AufAbschlagstyp
from ..enum.aufabschlagsziel import AufAbschlagsziel
from ..enum.waehrungseinheit import Waehrungseinheit
from .com import COM
from .energiemix import Energiemix
from .preisgarantie import Preisgarantie
from .regionalepreisstaffel import RegionalePreisstaffel
from .tarifeinschraenkung import Tarifeinschraenkung
from .vertragskonditionen import Vertragskonditionen
from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=no-name-in-module


# pylint: disable=R0801
class RegionalerAufAbschlag(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten
    abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert, die sich durch die Auswahl eines Auf-
    oder Abschlags ergeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalerAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalerAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalerAufAbschlag.json>`_

    """

    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: Optional[str] = None

    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    staffeln: Optional[list[RegionalePreisstaffel]] = None

    #: Beschreibung des Auf-/Abschlags
    beschreibung: Optional[str] = None

    #: Typ des Aufabschlages (z.B. absolut oder prozentual)
    auf_abschlagstyp: Optional[AufAbschlagstyp] = None

    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.
    auf_abschlagsziel: Optional[AufAbschlagsziel] = None

    #: Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird (nur im Falle absoluter Aufschlagstypen).
    einheit: Optional[Waehrungseinheit] = None

    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind
    website: Optional[str] = None

    #: Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhältlich sind
    zusatzprodukte: Optional[list[str]] = None

    #: Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann
    voraussetzungen: Optional[list[str]] = None

    #: Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten
    tarifnamensaenderungen: Optional[str] = None

    #: Zeitraum, in dem der Abschlag zur Anwendung kommen kann
    gueltigkeitszeitraum: Optional[Zeitraum] = None

    energiemixaenderung: Optional[Energiemix] = None
    """
    Der Energiemix kann sich durch einen AufAbschlag ändern (z.B. zwei Cent Aufschlag für Ökostrom).
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben.
    """

    vertagskonditionsaenderung: Optional[Vertragskonditionen] = None
    """
    Änderungen in den Vertragskonditionen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """

    garantieaenderung: Optional[Preisgarantie] = None
    """
    Änderungen in den Garantievereinbarungen;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """

    einschraenkungsaenderung: Optional[Tarifeinschraenkung] = None
    """
    Änderungen in den Einschränkungen zum Tarif;
    Falls in dieser Komponenten angegeben, werden die Tarifparameter hiermit überschrieben.
    """
