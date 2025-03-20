"""
Contains Regionaltarif class and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.typ import Typ
from .tarifinfo import Tarifinfo

if TYPE_CHECKING:
    from ..com.regionalepreisgarantie import RegionalePreisgarantie
    from ..com.regionaleraufabschlag import RegionalerAufAbschlag
    from ..com.regionaletarifpreisposition import RegionaleTarifpreisposition
    from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ..com.tarifeinschraenkung import Tarifeinschraenkung


# pylint: disable=too-few-public-methods, empty-docstring
# pylint: disable=no-name-in-module


class Regionaltarif(Tarifinfo):
    """
    Abbildung eines Tarifs mit regionaler Zuordnung von Preisen und Auf- und Abschlägen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Regionaltarif.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionaltarif JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Regionaltarif.json>`_

    """

    typ: Annotated[Literal[Typ.REGIONALTARIF], Field(alias="_typ")] = Typ.REGIONALTARIF  # type: ignore[assignment]
    preisstand: Optional[pydantic.AwareDatetime] = None
    """Gibt an, wann der Preis zuletzt angepasst wurde"""
    berechnungsparameter: Optional["Tarifberechnungsparameter"] = None
    """Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen"""
    tarifpreise: Optional[list["RegionaleTarifpreisposition"]] = None
    """Die festgelegten Preise mit regionaler Eingrenzung, z.B. für Arbeitspreis, Grundpreis etc."""

    tarif_auf_abschlaege: Optional[list["RegionalerAufAbschlag"]] = None
    """Auf- und Abschläge auf die Preise oder Kosten mit regionaler Eingrenzung"""
    preisgarantien: Optional[list["RegionalePreisgarantie"]] = None
    """Festlegung von Garantien für bestimmte Preisanteile"""
    tarifeinschraenkung: Optional["Tarifeinschraenkung"] = None
    """Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann"""
