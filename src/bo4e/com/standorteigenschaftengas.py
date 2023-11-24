"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from .com import COM
from .marktgebietinfo import MarktgebietInfo

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

    netzkontonummern: Optional[list[str]] = None  #: Netzkontonummern der Gasnetze
    marktgebiete: Optional[list[MarktgebietInfo]] = None  #: Die Informationen zu Marktgebieten in dem Netz.
