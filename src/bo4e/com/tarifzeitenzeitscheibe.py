"""
Contains TarifzeitenZeitscheibe class
"""

from typing import Annotated, List, Literal, Optional

from pydantic import Field

from .. import COM, ComTyp
from ..com.tarifzeit import Tarifzeit
from ..com.zeitraum import Zeitraum
from ..utils import postprocess_docstring


@postprocess_docstring
class TarifzeitenZeitscheibe(COM):
    """
    Eine Zeitscheibe innerhalb der Tarifzeiten mit zugehöriger Gültigkeit und Tarifzeitabschnitten.
    """
    typ: Annotated[Optional[Literal[ComTyp.TARIFZEITENZEITSCHEIBE]], Field(alias="_typ")] = (
        ComTyp.TARIFZEITENZEITSCHEIBE
    )
    """Typ dieser Zeitscheibe - Default 'TARIFZEITENZEITSCHEIBE'"""

    gueltigkeit: Optional[Zeitraum] = None
    """Zeitraum, in dem diese Zeitscheibe gültig ist"""

    tarifzeiten: Optional[List[Tarifzeit]] = None
    """Liste von Tarifzeiten, z. B. NT, HT oder weitere Zeitmodelle"""
