"""
Contains Geraet class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften


# pylint: disable=too-few-public-methods


class Geraet(COM):
    """
    Mit dieser Komponente werden alle Geräte modelliert, die keine Zähler sind.

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/GeraetSchema.json>`_

    """

    # optional attributes
    #: Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    geraetenummer: str = None
    #: Festlegung der Eigenschaften des Gerätes. Z.B. Wandler MS/NS.
    geraeteeigenschaften: Geraeteeigenschaften = None
