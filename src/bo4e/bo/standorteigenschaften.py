"""
Contains Standorteigenschaften class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.standorteigenschaftengas import StandorteigenschaftenGas
    from ..com.standorteigenschaftenstrom import StandorteigenschaftenStrom


@postprocess_docstring
class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Standorteigenschaften.svg" type="image/svg+xml"></object>

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Standorteigenschaften.json>`_

    """

    typ: Annotated[Literal[BoTyp.STANDORTEIGENSCHAFTEN], Field(alias="_typ")] = BoTyp.STANDORTEIGENSCHAFTEN
    eigenschaften_strom: Optional[list["StandorteigenschaftenStrom"]] = None
    """Eigenschaften zur Sparte Strom"""

    eigenschaften_gas: Optional["StandorteigenschaftenGas"] = None
    """Eigenschaften zur Sparte Gas"""
