"""
Contains Tarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import Annotated, List, Optional

from annotated_types import Len

from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.com.aufabschlagregional import AufAbschlagRegional
from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.com.tarifpreispositionproort import TarifpreispositionProOrt
from bo4e.enum.botyp import BoTyp

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class Tarif(Tarifinfo):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Tarif.json>`_

    """

    bo_typ: BoTyp = BoTyp.TARIF
    # required attributes
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter
    #: Die festgelegten Preise mit regionaler Eingrenzung z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: Annotated[list[TarifpreispositionProOrt], Len(1)]

    # optional attributes
    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: Optional[List[AufAbschlagRegional]] = None
    # todo: fix inconsistency: RegionalerAufAbschlag vs. AufAbschlagRegional
    # https://github.com/Hochfrequenz/BO4E-python/issues/345

    #: Preisgarantie für diesen Tarif
    preisgarantie: Optional[Preisgarantie] = None
    # todo: fix inconsistency with regionaltarif https://github.com/Hochfrequenz/BO4E-python/issues/346
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = None
