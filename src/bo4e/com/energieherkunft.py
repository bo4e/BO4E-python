"""
Contains Energieherkunft class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Annotated, Optional

from annotated_types import Gt, Lt

from bo4e.com.com import COM
from bo4e.enum.erzeugungsart import Erzeugungsart

# pylint: disable=no-name-in-module


# pylint: disable=too-few-public-methods


class Energieherkunft(COM):
    """
    Abbildung einer Energieherkunft

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energieherkunft.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energieherkunft JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Energieherkunft.json>`_

    """

    # required attributes
    #: Art der Erzeugung der Energie.
    erzeugungsart: Optional[Erzeugungsart] = None
    #: Prozentualer Anteil der jeweiligen Erzeugungsart.
    anteil_prozent: Optional[Decimal] = None
