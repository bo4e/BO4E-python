"""
Contains Dienstleistung class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.dienstleistungstyp import Dienstleistungstyp


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Dienstleistung(COM):
    """
    Abbildung einer abrechenbaren Dienstleistung.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Dienstleistung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Dienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Dienstleistung.json>`_

    """

    typ: Annotated[Literal[ComTyp.DIENSTLEISTUNG], Field(alias="_typ")] = ComTyp.DIENSTLEISTUNG

    dienstleistungstyp: Optional["Dienstleistungstyp"] = None
    """Kennzeichnung der Dienstleistung"""
    bezeichnung: Optional[str] = None
    """Bezeichnung der Dienstleistung"""
