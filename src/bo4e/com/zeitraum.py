"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import model_validator
from pydantic_core.core_schema import ValidationInfo

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

    # pylint: disable=unused-argument, no-self-argument
    @model_validator(mode="before")
    def time_range_possibilities(cls, model: dict, validation_info: ValidationInfo) -> dict:  # type:ignore[type-arg]
        """
        An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
        This functions checks for these conditions of a valid address.
        """
        values = model
        # todo: rewrite this to be more readable; just migrated to pydantic v2 without thinking too much about it
        # https://github.com/bo4e/BO4E-python/issues/480
        endzeitpunkt = values.get("endzeitpunkt")
        if (
            ("einheit" in values and values["einheit"])
            and ("dauer" in values and values["dauer"])
            and not (
                ("startdatum" in values and values["startdatum"])
                or ("enddatum" in values and values["enddatum"])
                or ("startzeitpunkt" in values and values["startzeitpunkt"])
                or endzeitpunkt
            )
        ):
            return model
        if (
            ("startdatum" in values and values["startdatum"])
            and ("enddatum" in values and values["enddatum"])
            and not (
                ("einheit" in values and values["einheit"])
                or ("dauer" in values and values["dauer"])
                or ("startzeitpunkt" in values and values["startzeitpunkt"])
                or endzeitpunkt
            )
        ):
            return model
        if (
            ("startzeitpunkt" in values and values["startzeitpunkt"])
            and ("endzeitpunkt" in values and model["endzeitpunkt"])
            and not (
                ("einheit" in values and values["einheit"])
                or ("dauer" in values and values["dauer"])
                or ("startdatum" in values and values["startdatum"])
                or ("enddatum" in values and values["enddatum"])
            )
        ):
            return model

        raise ValueError(
            """
            Please choose from one of the three possibilities to specify the timerange:
            - einheit and dauer
            - startdatum and enddatum
            - startzeitpunkt and endzeitpunkt
            """
        )
