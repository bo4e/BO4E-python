"""
Contains Geraet class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from bo4e.com.com import COM
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften

# pylint: disable=too-few-public-methods


class Geraet(COM):
    """
    Mit dieser Komponente werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Geraet.json>`_

    """

    # optional attributes
    #: Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    geraetenummer: Optional[str] = None
    #: Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS.
    geraeteeigenschaften: Optional[Geraeteeigenschaften] = None
