"""
Contains Marktgebietinfo class
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class MarktgebietInfo(COM):
    """
    Informationen zum Marktgebiet im Gas.

    .. raw:: html

        <object data="../_static/images/bo4e/com/MarktgebietInfo.svg" type="image/svg+xml"></object>

    .. HINT::
        `MarktgebietInfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/MarktgebietInfo.json>`_

    """

    typ: Annotated[Literal[ComTyp.MARKTGEBIETINFO], Field(alias="_typ")] = ComTyp.MARKTGEBIETINFO

    marktgebiet: Optional[str] = None
    """Der Name des Marktgebietes"""
    marktgebietcode: Optional[str] = None
    """Die standardisierte Codenummer des Marktgebietes"""
