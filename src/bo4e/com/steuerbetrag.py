"""
Contains Steuerbetrag class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.steuerkennzeichen import Steuerkennzeichen
    from ..enum.waehrungscode import Waehrungscode


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Steuerbetrag(COM):
    """
    Abbildung eines Steuerbetrages.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Steuerbetrag.svg" type="image/svg+xml"></object>

    .. HINT::
        `Steuerbetrag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Steuerbetrag.json>`_

    """

    typ: Annotated[Literal[ComTyp.STEUERBETRAG], Field(alias="_typ")] = ComTyp.STEUERBETRAG

    steuerkennzeichen: Optional["Steuerkennzeichen"] = None
    """Kennzeichnung des Steuersatzes, bzw. Verfahrens."""
    basiswert: Optional[Decimal] = None
    """Nettobetrag für den die Steuer berechnet wurde. Z.B. 100"""
    steuerwert: Optional[Decimal] = None
    """Aus dem Basiswert berechnete Steuer. Z.B. 19 (bei UST_19)"""
    waehrung: Optional["Waehrungscode"] = None
    """Währung. Z.B. Euro."""
