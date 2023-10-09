"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from bo4e.com.com import COM
from bo4e.com.zeitspanne import Zeitspanne
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

    zeitspanne: Optional[Zeitspanne] = None  #: Zeitespanne für das Messintervall

    wert: Optional[Decimal] = None  #: Der im Zeitintervall gültige Wert.

    #: Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen.
    status: Optional[Messwertstatus] = None

    #: Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert.
    statuszusatz: Optional[Messwertstatuszusatz] = None
