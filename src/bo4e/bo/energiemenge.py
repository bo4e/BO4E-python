"""
Contains Energiemenge class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.menge import Menge
    from ..com.zeitraum import Zeitraum


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
    obis_kennzahl: Optional[str] = None
    """Die OBIS-Kennzahl der Energiemenge"""
    beschreibung: Optional[str] = None
    """Ergänzende Beschreibung zur Energiemenge"""
    zeitraum: Optional["Zeitraum"] = None
    """Zeitraum, in dem die Energiemenge angefallen ist/gemessen wurde"""
    menge: Optional["Menge"] = None
    """Die angefallene/gemessene Menge"""
