"""
Contains Tarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import List, Optional


from marshmallow import fields

from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.com.aufabschlagregional import AufAbschlagRegional
from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.com.tarifpreispositionproort import TarifpreispositionProOrt
from bo4e.enum.botyp import BoTyp
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
from pydantic import conlist


class Tarif(Tarifinfo):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/TarifSchema.json>`_

    """

    bo_typ: BoTyp = BoTyp.TARIF
    # required attributes
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter
    #: Die festgelegten Preise mit regionaler Eingrenzung z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: conlist(TarifpreispositionProOrt, min_items=1)

    # optional attributes
    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: List[AufAbschlagRegional] = None
    # todo: fix inconsistency: RegionalerAufAbschlag vs. AufAbschlagRegional
    # https://github.com/Hochfrequenz/BO4E-python/issues/345

    #: Preisgarantie für diesen Tarif
    preisgarantie: Preisgarantie = None
    # todo: fix inconsistency with regionaltarif https://github.com/Hochfrequenz/BO4E-python/issues/346
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Tarifeinschraenkung = None
