"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Optional

from annotated_types import Len

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas
from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom
from bo4e.enum.botyp import BoTyp


class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Standorteigenschaften.svg" type="image/svg+xml"></object>

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Standorteigenschaften.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.STANDORTEIGENSCHAFTEN
    #: Eigenschaften zur Sparte Strom
    eigenschaften_strom: Annotated[list[StandorteigenschaftenStrom], Len(1)]

    # optional attributes
    #: Eigenschaften zur Sparte Gas
    eigenschaften_gas: Optional[StandorteigenschaftenGas] = None
