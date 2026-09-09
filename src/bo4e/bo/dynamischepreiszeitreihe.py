"""
Contains DynamischePreiszeitreihe class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from bo4e import Geschaeftsobjekt
from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring

if TYPE_CHECKING:
    from ..com.preiszeitreihe import Preiszeitreihe
    from .marktlokation import Marktlokation
    from .zaehler import Zaehler


@postprocess_docstring
class DynamischePreiszeitreihe(Geschaeftsobjekt):
    """
    Abbildung einer dynamischen Preiszeitreihe.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/DynamischePreiszeitreihe.svg" type="image/svg+xml"></object>

    .. HINT::
        `DynamischePreiszeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/DynamischePreiszeitreihe.json>`_

    """

    typ: Annotated[Literal[BoTyp.DYNAMISCHE_PREISZEITREIHE], Field(alias="_typ")] = BoTyp.DYNAMISCHE_PREISZEITREIHE

    marktlokation: Optional["Marktlokation"] = None
    """Marktlokation der dynamischen Preiszeitreihe"""
    zaehler: Optional["Zaehler"] = None
    """Zaehler der dynamischen Preiszeitreihe"""
    preiszeitreihen: list["Preiszeitreihe"] | None = None
    """Werte der Preiszeitreihe"""
