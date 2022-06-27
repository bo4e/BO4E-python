"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.com.com import COM
from bo4e.com.marktgebietinfo import MarktgebietInfo


class StandorteigenschaftenGas(COM):
    """
    Standorteigenschaften der Sparte Gas

    .. graphviz:: /api/dots/bo4e/com/StandorteigenschaftenGas.dot

    """

    # required attributes
    netzkontonummern: conlist(str, min_items=1, max_items=2)  #: Netzkontonummern der Gasnetze
    marktgebiete: List[MarktgebietInfo]  #: Die Informationen zu Marktgebieten in dem Netz.
