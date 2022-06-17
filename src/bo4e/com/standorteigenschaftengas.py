"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List


from bo4e.com.com import COM
from bo4e.com.marktgebietinfo import MarktgebietInfo

# pylint: disable=too-few-public-methods
from pydantic import conlist


class StandorteigenschaftenGas(COM):
    """
    Standorteigenschaften der Sparte Gas

    .. HINT::
        `StandorteigenschaftenGas JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/StandorteigenschaftenGasSchema.json>`_

    """

    # required attributes
    netzkontonummern: conlist(str, min_items=1, max_items=2)  #: Netzkontonummern der Gasnetze
    marktgebiete: List[MarktgebietInfo]  #: Die Informationen zu Marktgebieten in dem Netz.
