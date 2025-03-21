"""
Contains Preis class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.preisstatus import Preisstatus
    from ..enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preis(COM):
    """
    Abbildung eines Preises mit Wert, Einheit, Bezugswert und Status.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preis.json>`_

    """

    typ: Annotated[Literal[ComTyp.PREIS], Field(alias="_typ")] = ComTyp.PREIS

    wert: Optional[Decimal] = None
    """Gibt die nominale Höhe des Preises an."""
    einheit: Optional["Waehrungseinheit"] = None
    """Währungseinheit für den Preis, z.B. Euro oder Ct."""
    bezugswert: Optional["Mengeneinheit"] = None
    """Angabe, für welche Bezugsgröße der Preis gilt. Z.B. kWh."""

    status: Optional["Preisstatus"] = None
    """Gibt den Status des veröffentlichten Preises an"""
