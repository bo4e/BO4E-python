"""
Contains Hardware class
and corresponding marshmallow schema for de-/serialization
"""


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods


class Hardware(COM):
    """
    Abbildung einer abrechenbaren Hardware

    .. HINT::
        `Hardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/HardwareSchema.json>`_

    """

    # required attributes
    #: Eindeutiger Typ der Hardware
    geraetetyp: Geraetetyp
    #: Bezeichnung der Hardware
    bezeichnung: str
