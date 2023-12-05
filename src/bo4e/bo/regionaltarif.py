"""
Contains Regionaltarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.regionalepreisgarantie import RegionalePreisgarantie
from ..com.regionaleraufabschlag import RegionalerAufAbschlag
from ..com.regionaletarifpreisposition import RegionaleTarifpreisposition
from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
from ..com.tarifeinschraenkung import Tarifeinschraenkung
from ..enum.typ import Typ
from .tarifinfo import Tarifinfo

# pylint: disable=too-few-public-methods, empty-docstring
# pylint: disable=no-name-in-module


class Regionaltarif(Tarifinfo):
    #: Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen.
    """

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Regionaltarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionaltarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Regionaltarif.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.REGIONALTARIF
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: Optional[datetime] = None
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Optional[Tarifberechnungsparameter] = None
    #: Die festgelegten Preise mit regionaler Eingrenzung, z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: Optional[list[RegionaleTarifpreisposition]] = None

    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: Optional[list[RegionalerAufAbschlag]] = None
    #: Festlegung von Garantien für bestimmte Preisanteile
    preisgarantien: Optional[list[RegionalePreisgarantie]] = None
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = None
