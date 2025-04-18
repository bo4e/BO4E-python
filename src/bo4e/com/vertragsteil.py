"""
Contains Vertragsteil class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .menge import Menge

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Vertragsteil(COM):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragsteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Vertragsteil.json>`_

    """

    typ: Annotated[Literal[ComTyp.VERTRAGSTEIL], Field(alias="_typ")] = ComTyp.VERTRAGSTEIL

    vertragsteilbeginn: Optional[pydantic.AwareDatetime] = None
    """
    Start der Gültigkeit des Vertragsteils (inklusiv)
    """
    vertragsteilende: Optional[pydantic.AwareDatetime] = None
    """
    Ende der Gültigkeit des Vertragsteils (exklusiv)
    """

    lokation: Optional[str] = None
    """
    Der Identifier für diejenigen Markt- oder Messlokation, die zu diesem Vertragsteil gehören.
    Verträge für mehrere Lokationen werden mit mehreren Vertragsteilen abgebildet
    """
    vertraglich_fixierte_menge: Optional["Menge"] = None
    """
    Für die Lokation festgeschriebene Abnahmemenge
    """
    minimale_abnahmemenge: Optional["Menge"] = None
    """
    Für die Lokation festgelegte Mindestabnahmemenge (inklusiv)
    """
    maximale_abnahmemenge: Optional["Menge"] = None
    """
    Für die Lokation festgelegte maximale Abnahmemenge (exklusiv)
    """
