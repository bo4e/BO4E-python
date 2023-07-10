"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, List

from annotated_types import Len

from bo4e.com.com import COM
from bo4e.com.marktgebietinfo import MarktgebietInfo

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


class StandorteigenschaftenGas(COM):
    """
    Standorteigenschaften der Sparte Gas

    .. raw:: html

        <object data="../_static/images/bo4e/com/StandorteigenschaftenGas.svg" type="image/svg+xml"></object>

    .. HINT::
        `StandorteigenschaftenGas JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/StandorteigenschaftenGas.json>`_

    """

    # required attributes
    netzkontonummern: Annotated[list[str], Len(1, 2)]  #: Netzkontonummern der Gasnetze
    marktgebiete: List[MarktgebietInfo]  #: Die Informationen zu Marktgebieten in dem Netz.
