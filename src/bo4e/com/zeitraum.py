"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.zeiteinheit import Zeiteinheit
from bo4e.validators import combinations_of_fields

# pylint: disable=too-few-public-methods


class Zeitraum(COM):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitraum.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitraum JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zeitraum.json>`_

    """

    # optional attributes
    einheit: Optional[Zeiteinheit] = None
    dauer: Optional[Decimal] = None
    startdatum: Optional[datetime] = None
    enddatum: Optional[datetime] = None
    startzeitpunkt: Optional[datetime] = None
    endzeitpunkt: Optional[datetime] = None

    _time_range_possibilities = combinations_of_fields(
        "einheit",
        "dauer",
        "startdatum",
        "enddatum",
        "startzeitpunkt",
        "endzeitpunkt",
        valid_combinations={
            (1, 1, 0, 0, 0, 0),
            (0, 0, 1, 1, 0, 0),
            (0, 0, 0, 0, 1, 1),
        },
        custom_error_message="""
        Please choose from one of the three possibilities to specify the timerange:
        - einheit and dauer
        - startdatum and enddatum
        - startzeitpunkt and endzeitpunkt
        """,
    )
    """
    Validator that ensures that exactly one of the three possibilities to specify the timerange is chosen.
        - einheit and dauer
        - startdatum and enddatum
        - startzeitpunkt and endzeitpunkt
    """
