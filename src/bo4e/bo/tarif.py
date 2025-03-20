"""
Contains Tarif class and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .tarifinfo import Tarifinfo

if TYPE_CHECKING:
    from ..com.aufabschlagregional import AufAbschlagRegional
    from ..com.preisgarantie import Preisgarantie
    from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ..com.tarifeinschraenkung import Tarifeinschraenkung
    from ..com.tarifpreispositionproort import TarifpreispositionProOrt


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Tarif(Tarifinfo):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarif.json>`_

    """

    typ: Annotated[Literal[Typ.TARIF], Field(alias="_typ")] = Typ.TARIF  # type: ignore[assignment]
    preisstand: Optional[pydantic.AwareDatetime] = None
    """Gibt an, wann der Preis zuletzt angepasst wurde"""
    berechnungsparameter: Optional["Tarifberechnungsparameter"] = None
    """Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen"""
    tarifpreise: Optional[list["TarifpreispositionProOrt"]] = None
    """Die festgelegten Preise mit regionaler Eingrenzung z.B. für Arbeitspreis, Grundpreis etc."""

    tarif_auf_abschlaege: Optional[list["AufAbschlagRegional"]] = None
    """Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung"""
    # todo: fix inconsistency: RegionalerAufAbschlag vs. AufAbschlagRegional
    # https://github.com/Hochfrequenz/BO4E-python/issues/345

    preisgarantie: Optional["Preisgarantie"] = None
    """Preisgarantie für diesen Tarif"""
    # todo: fix inconsistency with regionaltarif https://github.com/Hochfrequenz/BO4E-python/issues/346
    tarifeinschraenkung: Optional["Tarifeinschraenkung"] = None
    """Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann"""
