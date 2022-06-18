"""
Contains Tarifpreisblatt class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import List

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.com.aufabschlag import AufAbschlag
from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.com.tarifpreisposition import Tarifpreisposition
from bo4e.enum.botyp import BoTyp


class Tarifpreisblatt(Tarifinfo):
    """
    Tarifinformation mit Preisen, Aufschlägen und Berechnungssystematik

    .. HINT::
        `Tarifpreisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/TarifpreisblattSchema.json>`_

    """

    bo_typ: BoTyp = BoTyp.TARIFPREISBLATT
    # required attributes (additional to those of Tarifinfo)
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime
    #: Die festgelegten Preise, z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: conlist(Tarifpreisposition, min_items=1)
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter

    # optional attributes
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Tarifeinschraenkung = None
    #: Festlegung von Garantien für bestimmte Preisanteile
    preisgarantie: Preisgarantie = None
    #: Auf- und Abschläge auf die Preise oder Kosten
    tarif_auf_abschlaege: List[AufAbschlag] = None
