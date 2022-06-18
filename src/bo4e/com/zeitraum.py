"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from decimal import Decimal

from pydantic import validator

from bo4e.com.com import COM
from bo4e.enum.zeiteinheit import Zeiteinheit


# pylint: disable=too-few-public-methods


class Zeitraum(COM):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)

    .. HINT::
        `Zeitraum JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZeitraumSchema.json>`_

    """

    # optional attributes
    einheit: Zeiteinheit = None
    dauer: Decimal = None
    startdatum: datetime = None
    enddatum: datetime = None
    startzeitpunkt: datetime = None
    endzeitpunkt: datetime = None

    # pylint: disable=unused-argument
    # pylint: disable=no-self-argument
    @validator("endzeitpunkt", always=True)
    def time_range_possibilities(cls, endzeitpunkt, values):
        """
        An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
        This functions checks for these conditions of a valid address.
        """

        if (
            values["einheit"]
            and values["dauer"]
            and not (values["startdatum"] or values["enddatum"] or values["startzeitpunkt"] or endzeitpunkt)
        ):
            return endzeitpunkt
        if (
            values["startdatum"]
            and values["enddatum"]
            and not (values["einheit"] or values["dauer"] or values["startzeitpunkt"] or endzeitpunkt)
        ):
            return endzeitpunkt
        if (
            values["startzeitpunkt"]
            and endzeitpunkt
            and not (values["einheit"] or values["dauer"] or values["startdatum"] or values["enddatum"])
        ):
            return endzeitpunkt

        raise ValueError(
            """
            Please choose from one of the three possibilities to specify the timerange:
            - einheit and dauer
            - startdatum and enddatum
            - startzeitpunkt and endzeitpunkt
            """
        )
