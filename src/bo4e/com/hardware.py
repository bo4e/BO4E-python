"""
Contains Hardware class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods


class Hardware(COM):
    """
    Abbildung einer abrechenbaren Hardware

    .. graphviz:: /api/dots/bo4e/com/Hardware.dot

    """

    # required attributes
    #: Eindeutiger Typ der Hardware
    geraetetyp: Geraetetyp
    #: Bezeichnung der Hardware
    bezeichnung: str
