"""
Contains Tarifzeitstufe class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.zeitraum import Zeitraum


@postprocess_docstring
class Tarifzeitstufe(COM):
    """
    Tarifzeitstufe mit Zuordnung zu einem Zeitraum und einer optionalen Tarifstufe.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifzeitstufe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifzeitstufe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarifzeitstufe.json>`_

    """

    typ: Annotated[Optional[Literal[ComTyp.TARIFZEITSTUFE]], Field(alias="_typ")] = ComTyp.TARIFZEITSTUFE

    zeitraum: Optional["Zeitraum"] = None
    """Gültigkeitszeitraum der Tarifzeitstufe"""

    tarifstufe: Optional[str] = None
    """Optional: Angabe der Tarifstufe, z. B. HT, NT, ST"""
