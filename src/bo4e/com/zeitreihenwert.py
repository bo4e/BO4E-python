"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

from .zeitreihenwertkompakt import Zeitreihenwertkompakt

# pylint: disable=too-few-public-methods


class Zeitreihenwert(Zeitreihenwertkompakt):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitreihenwert.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zeitreihenwert.json>`_

    """

    datum_uhrzeit_von: Optional[
        datetime
    ] = None  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall begonnen wurde (inklusiv)
    datum_uhrzeit_bis: Optional[
        datetime
    ] = None  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall endet (exklusiv)
