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
    from ..enum.steuerart import Steuerart
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

    steuerart: Optional["Steuerart"] = None
    """Kennzeichnung der Steuerart, bzw. Verfahrens."""
    steuersatz: Optional[Decimal] = None
    """Angabe des Steuersatzes in %"""
    basiswert: Optional[Decimal] = None
    """Nettobetrag für den die Steuer berechnet wurde. Z.B. 100"""
    steuerwert: Optional[Decimal] = None
    """Aus dem Basiswert berechnete Steuer. Z.B. 19 (bei UST_19)"""
    waehrungscode: Optional["Waehrungscode"] = None
    """Währung. Z.B. Euro."""
