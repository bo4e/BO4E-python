"""
Contains Katasteradresse class
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Katasteradresse(COM):
    """
    Dient der Adressierung über die Liegenschafts-Information.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Katasteradresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Katasteradresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Katasteradresse.json>`_

    """

    typ: Annotated[Literal[ComTyp.KATASTERADRESSE], Field(alias="_typ")] = ComTyp.KATASTERADRESSE

    gemarkung_flur: Optional[str] = None
    flurstueck: Optional[str] = None
