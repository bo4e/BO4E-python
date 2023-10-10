"""
Contains Zeitreihenwertkompakt class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from ..enum.messwertstatus import Messwertstatus
from ..enum.messwertstatuszusatz import Messwertstatuszusatz
from .com import COM

# pylint: disable=too-few-public-methods


class Zeitreihenwertkompakt(COM):
    """
    Abbildung eines kompakten Zeitreihenwertes in dem ausschliesslich der Wert und Statusinformationen stehen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitreihenwertkompakt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihenwertkompakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zeitreihenwertkompakt.json>`_

    """

    wert: Optional[Decimal] = None  #: Der im Zeitintervall gültige Wert.

    #: Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen.
    status: Optional[Messwertstatus] = None

    #: Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert.
    statuszusatz: Optional[Messwertstatuszusatz] = None
