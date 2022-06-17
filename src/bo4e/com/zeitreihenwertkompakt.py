"""
Contains Zeitreihenwertkompakt class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional


from bo4e.com.com import COM
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz


# pylint: disable=too-few-public-methods


class Zeitreihenwertkompakt(COM):
    """
    Abbildung eines kompakten Zeitreihenwertes in dem ausschliesslich der Wert und Statusinformationen stehen.

    .. HINT::
        `Zeitreihenwertkompakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZeitreihenwertkompaktSchema.json>`_

    """

    # required attributes
    wert: Decimal  #: Der im Zeitintervall gültige Wert.

    # optional attributes
    status: Messwertstatus = None  #: Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen.

    statuszusatz: Messwertstatuszusatz = (
        None  #: Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert.
    )
