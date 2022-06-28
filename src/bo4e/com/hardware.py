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

    .. HINT::
        `Hardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Hardware.json>`_

    """

    # required attributes
    #: Eindeutiger Typ der Hardware
    geraetetyp: Geraetetyp
    #: Bezeichnung der Hardware
    bezeichnung: str
