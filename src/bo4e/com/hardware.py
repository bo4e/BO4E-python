"""
Contains Hardware class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.geraetetyp import Geraetetyp

# pylint: disable=too-few-public-methods


class Hardware(COM):
    """
    Abbildung einer abrechenbaren Hardware

    .. raw:: html

        <object data="../_static/images/bo4e/com/Hardware.svg" type="image/svg+xml"></object>

    .. HINT::
        `Hardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Hardware.json>`_

    """

    #: Eindeutiger Typ der Hardware
    geraetetyp: Optional[Geraetetyp] = None
    #: Bezeichnung der Hardware
    bezeichnung: Optional[str] = None
