"""
Contains Tarif class and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.aufabschlagregional import AufAbschlagRegional
from ..com.preisgarantie import Preisgarantie
from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
from ..com.tarifeinschraenkung import Tarifeinschraenkung
from ..com.tarifpreispositionproort import TarifpreispositionProOrt
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .tarifinfo import Tarifinfo

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Tarif(Tarifinfo):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarif.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.TARIF
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: Optional[datetime] = None
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Optional[Tarifberechnungsparameter] = None
    #: Die festgelegten Preise mit regionaler Eingrenzung z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: Optional[list[TarifpreispositionProOrt]] = None

    #: Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung
    tarif_auf_abschlaege: Optional[list[AufAbschlagRegional]] = None
    # todo: fix inconsistency: RegionalerAufAbschlag vs. AufAbschlagRegional
    # https://github.com/Hochfrequenz/BO4E-python/issues/345

    #: Preisgarantie für diesen Tarif
    preisgarantie: Optional[Preisgarantie] = None
    # todo: fix inconsistency with regionaltarif https://github.com/Hochfrequenz/BO4E-python/issues/346
    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = None
