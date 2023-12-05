"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from pydantic import Field

from ..com.standorteigenschaftengas import StandorteigenschaftenGas
from ..com.standorteigenschaftenstrom import StandorteigenschaftenStrom
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


@postprocess_docstring
class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Standorteigenschaften.svg" type="image/svg+xml"></object>

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Standorteigenschaften.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.STANDORTEIGENSCHAFTEN
    #: Eigenschaften zur Sparte Strom
    eigenschaften_strom: Optional[list[StandorteigenschaftenStrom]] = None

    #: Eigenschaften zur Sparte Gas
    eigenschaften_gas: Optional[StandorteigenschaftenGas] = None
