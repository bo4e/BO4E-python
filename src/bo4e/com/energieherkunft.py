"""
Contains Energieherkunft class
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=no-name-in-module
from pydantic import condecimal

from bo4e.com.com import COM
from bo4e.enum.erzeugungsart import Erzeugungsart

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
    erzeugungsart: Erzeugungsart
    #: Prozentualer Anteil der jeweiligen Erzeugungsart.
    anteil_prozent: condecimal(gt=0, lt=100)  # type: ignore[valid-type]
