"""
Contains TarifzeitenZeitscheibe class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.tarifzeitstufe import Tarifzeitstufe
    from ..com.zeitraum import Zeitraum


@postprocess_docstring
class TarifzeitenZeitscheibe(COM):
    """
    Eine Zeitscheibe innerhalb der Tarifzeiten mit zugehöriger Gültigkeit und Tarifzeitabschnitten.

    .. raw:: html

        <object data="../_static/images/bo4e/com/TarifzeitenZeitscheibe.svg" type="image/svg+xml"></object>

    .. HINT::
        `TarifzeitenZeitscheibe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/TarifzeitenZeitscheibe.json>`_

    """

    typ: Annotated[Optional[Literal[ComTyp.TARIFZEITENZEITSCHEIBE]], Field(alias="_typ")] = (
        ComTyp.TARIFZEITENZEITSCHEIBE
    )

    gueltigkeit: Optional["Zeitraum"] = None
    """Zeitraum, in dem diese Zeitscheibe gültig ist"""

    tarifzeiten: Optional[list["Tarifzeitstufe"]] = None
    """Liste von Tarifzeitenstufen, z. B. NT, HT oder weitere Zeitmodelle"""
