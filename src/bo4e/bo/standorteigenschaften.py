"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Optional

from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein
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
    #: Allgemeine Eigenschaften
    eigenschaften_allgemein: StandorteigenschaftenAllgemein
    #: Eigenschaften zur Sparte Strom
    eigenschaften_strom: conlist(StandorteigenschaftenStrom, min_items=1)  # type: ignore[valid-type]

    # optional attributes
    #: Eigenschaften zur Sparte Gas
    eigenschaften_gas: Optional[StandorteigenschaftenGas] = None
