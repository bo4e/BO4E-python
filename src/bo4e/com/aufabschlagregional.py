"""
Contains AufAbschlagRegional and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.aufabschlagproort import AufAbschlagProOrt
from bo4e.com.com import COM
from bo4e.com.energiemix import Energiemix
from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
from pydantic import conlist


class AufAbschlagRegional(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen
    im Zusammenhang mit regionalen Gültigkeiten abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert,
    die sich durch die Auswahl eines Auf- oder Abschlags ergeben.

    .. HINT::
        `AufAbschlagRegional JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagRegionalSchema.json>`_

    """

    # required attributess
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str
    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    betraege: conlist(AufAbschlagProOrt, min_items=1)

    # optional attributes
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: str = None
    #:Typ des Aufabschlages (z.B. absolut oder prozentual)
    auf_abschlagstyp: AufAbschlagstyp = None
    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc.
    auf_abschlagsziel: AufAbschlagsziel = None
    #: Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct.
    einheit: Waehrungseinheit = None
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind
    website: str = None
    #: Zusatzprodukte, die nur in Kombination mit diesem AufAbschlag erhältlich sind
    zusatzprodukte: List[str] = None
    #: Voraussetzungen, die erfüllt sein müssen, damit dieser AufAbschlag zur Anwendung kommen kann
    voraussetzungen: List[str] = None
    #: Durch die Anwendung des Auf/Abschlags kann eine Änderung des Tarifnamens auftreten.
    tarifnamensaenderungen: str = None
    #: Zeitraum, in dem der Abschlag zur Anwendung kommen kann
    gueltigkeitszeitraum: Zeitraum = None
    energiemixaenderung: Energiemix = None
    """ Der Energiemix kann sich durch einen AufAbschlag ändern (z.B. zwei Cent Aufschlag für Ökostrom:
    Sollte dies der Fall sein, wird hier die neue Zusammensetzung des Energiemix angegeben."""
    vertagskonditionsaenderung: Vertragskonditionen = None
    """ Änderungen in den Vertragskonditionen. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben."""
    garantieaenderung: Preisgarantie = None
    """ Änderungen in den Garantievereinbarungen. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben."""
    einschraenkungsaenderung: Tarifeinschraenkung = None
    """ Änderungen in den Einschränkungen zum Tarif. Falls in dieser Komponenten angegeben,
    werden die Tarifparameter hiermit überschrieben."""
