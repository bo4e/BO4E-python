"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.enum.zeiteinheit import Zeiteinheit


# pylint: disable=unused-argument
def time_range_possibilities(instance, attribute, value):
    """
    An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
    This functions checks for these conditions of a valid address.
    """

    if (
        instance.einheit
        and instance.dauer
        and not (instance.startdatum or instance.enddatum or instance.startzeitpunkt or instance.endzeitpunkt)
    ):
        return
    if (
        instance.startdatum
        and instance.enddatum
        and not (instance.einheit or instance.dauer or instance.startzeitpunkt or instance.endzeitpunkt)
    ):
        return
    if (
        instance.startzeitpunkt
        and instance.endzeitpunkt
        and not (instance.einheit or instance.dauer or instance.startdatum or instance.enddatum)
    ):
        return

    raise ValueError(
        """
        Please choose from one of the three possibilities to specify the timerange:
        - einheit and dauer
        - startdatum and enddatum
        - startzeitpunkt and endzeitpunkt
        """
    )


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
    einheit: Zeiteinheit = attrs.field(default=None, validator=time_range_possibilities)
    dauer: Decimal = attrs.field(default=None, validator=time_range_possibilities)
    startdatum: datetime = attrs.field(default=None, validator=time_range_possibilities)
    enddatum: datetime = attrs.field(default=None, validator=time_range_possibilities)
    startzeitpunkt: datetime = attrs.field(default=None, validator=time_range_possibilities)
    endzeitpunkt: datetime = attrs.field(default=None, validator=time_range_possibilities)
