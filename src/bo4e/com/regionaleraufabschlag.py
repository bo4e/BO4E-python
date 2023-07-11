"""
Contains RegionalerAufAbschlag class and corresponding marshmallow schema for de-/serialization
"""

from typing import Annotated, List, Optional

from annotated_types import Len

from bo4e.com.com import COM
from bo4e.com.energiemix import Energiemix
from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit

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

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str

    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    staffeln: Annotated[list[RegionalePreisstaffel], Len(1)]

    # optional attributes
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
    zusatzprodukte: Optional[List[str]] = None

    #: Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann
    voraussetzungen: Optional[List[str]] = None

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
