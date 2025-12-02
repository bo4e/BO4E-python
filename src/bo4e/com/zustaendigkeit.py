"""
Contains Zustaendigkeit class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.themengebiet import Themengebiet


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Zustaendigkeit(COM):
    """
    Enthält die zeitliche Zuordnung eines Ansprechpartners zu Abteilungen und Zuständigkeiten.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zustaendigkeit.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zustaendigkeit JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zustaendigkeit.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZUSTAENDIGKEIT], Field(alias="_typ")] = ComTyp.ZUSTAENDIGKEIT
    themengebiet: Optional["Themengebiet"] = None
    """
    Hier kann eine thematische Zuordnung des Ansprechpartners bzw. der Person angegeben werden
    """

    position: Optional[str] = None
    """Berufliche Rolle des Ansprechpartners/ der Person"""
    abteilung: Optional[str] = None
    """Abteilung, in der der Ansprechpartner/ die Person tätig ist"""
