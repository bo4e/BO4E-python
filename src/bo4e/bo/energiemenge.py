"""
Contains Energiemenge class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.verbrauch import Verbrauch
    from ..enum.lokationstyp import Lokationstyp


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Energiemenge(Geschaeftsobjekt):
    """
    Abbildung von Mengen, die Lokationen zugeordnet sind

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Energiemenge.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energiemenge JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Energiemenge.json>`_

    """

    typ: Annotated[Literal[BoTyp.ENERGIEMENGE], Field(alias="_typ")] = BoTyp.ENERGIEMENGE
    lokations_id: Optional[str] = None
    """Eindeutige Nummer der Marktlokation bzw. der Messlokation, zu der die Energiemenge gehört"""
    lokationstyp: Optional["Lokationstyp"] = None
    """Gibt an, ob es sich um eine Markt- oder Messlokation handelt"""

    energieverbrauch: Optional[list["Verbrauch"]] = None
    """Gibt den Verbrauch in einer Zeiteinheit an"""
    # there are no optional attributes
