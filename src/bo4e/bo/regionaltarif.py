"""
Contains Regionaltarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import Annotated, List, Optional

from annotated_types import Len

from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.com.regionalepreisgarantie import RegionalePreisgarantie
from bo4e.com.regionaleraufabschlag import RegionalerAufAbschlag
from bo4e.com.regionaletarifpreisposition import RegionaleTarifpreisposition
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.enum.botyp import BoTyp

# pylint: disable=too-few-public-methods, empty-docstring
# pylint: disable=no-name-in-module


class Regionaltarif(Tarifinfo):
    #: Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen.
    """

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Regionaltarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionaltarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Regionaltarif.json>`_

    """

    bo_typ: BoTyp = BoTyp.REGIONALTARIF
    # required attributes
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: datetime
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Tarifberechnungsparameter
    #: Die festgelegten Preise mit regionaler Eingrenzung, z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: Annotated[list[RegionaleTarifpreisposition], Len(1)]

    # optional attributes
    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: Optional[List[RegionalerAufAbschlag]] = None
    #: Festlegung von Garantien für bestimmte Preisanteile
    preisgarantien: Optional[List[RegionalePreisgarantie]] = None
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = None
