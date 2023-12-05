"""
Contains Energieherkunft class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from ..enum.erzeugungsart import Erzeugungsart
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=no-name-in-module


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Energieherkunft(COM):
    """
    Abbildung einer Energieherkunft

    .. raw:: html

        <object data="../_static/images/bo4e/com/Energieherkunft.svg" type="image/svg+xml"></object>

    .. HINT::
        `Energieherkunft JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Energieherkunft.json>`_

    """

    #: Art der Erzeugung der Energie.
    erzeugungsart: Optional[Erzeugungsart] = None
    #: Prozentualer Anteil der jeweiligen Erzeugungsart.
    anteil_prozent: Optional[Decimal] = None
