"""
Contains Tarifpreisblatt class and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .tarifinfo import Tarifinfo

if TYPE_CHECKING:
    from ..com.aufabschlag import AufAbschlag
    from ..com.preisgarantie import Preisgarantie
    from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
    from ..com.tarifeinschraenkung import Tarifeinschraenkung
    from ..com.tarifpreisposition import Tarifpreisposition


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Tarifpreisblatt(Tarifinfo):
    """
    Tarifinformation mit Preisen, Aufschlägen und Berechnungssystematik

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifpreisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarifpreisblatt.json>`_

    """

    typ: Annotated[Literal[Typ.TARIFPREISBLATT], Field(alias="_typ")] = Typ.TARIFPREISBLATT  # type: ignore[assignment]
    # required attributes (additional to those of Tarifinfo)
    preisstand: Optional[pydantic.AwareDatetime] = None
    """Gibt an, wann der Preis zuletzt angepasst wurde"""
    tarifpreise: Optional[list["Tarifpreisposition"]] = None
    """Die festgelegten Preise, z.B. für Arbeitspreis, Grundpreis etc."""
    berechnungsparameter: Optional["Tarifberechnungsparameter"] = None
    """Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen"""

    tarifeinschraenkung: Optional["Tarifeinschraenkung"] = None
    """Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann"""
    preisgarantie: Optional["Preisgarantie"] = None
    """Festlegung von Garantien für bestimmte Preisanteile"""
    tarif_auf_abschlaege: Optional[list["AufAbschlag"]] = None
    """Auf- und Abschläge auf die Preise oder Kosten"""
