"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz

# pylint: disable=too-few-public-methods


class Zeitreihenwert(COM):
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

    wert: Optional[Decimal] = None  #: Der im Zeitintervall gültige Wert.

    #: Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen.
    status: Optional[Messwertstatus] = None

    #: Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert.
    statuszusatz: Optional[Messwertstatuszusatz] = None
