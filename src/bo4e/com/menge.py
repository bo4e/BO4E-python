"""
Contains Menge class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Menge(COM):
    """
    Abbildung einer Menge mit Wert und Einheit.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Menge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Menge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Menge.json>`_

    """

    typ: Annotated[Literal[ComTyp.MENGE], Field(alias="_typ")] = ComTyp.MENGE

    wert: Optional[Decimal] = None
    """Gibt den absoluten Wert der Menge an"""
    einheit: Optional["Mengeneinheit"] = None
    """Gibt die Einheit zum jeweiligen Wert an"""
