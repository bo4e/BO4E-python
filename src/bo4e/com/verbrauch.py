"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import Field, field_validator
from pydantic_core.core_schema import ValidationInfo

from bo4e.com.com import COM
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from bo4e.validators import OBIS_PATTERN, check_bis_is_later_than_von


class Verbrauch(COM):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verbrauch.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Verbrauch.json>`_

    """

    # required attributes
    #: Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt
    wertermittlungsverfahren: Wertermittlungsverfahren
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:
    obis_kennzahl: Annotated[str, Field(strict=True, pattern=OBIS_PATTERN)]
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal
    #: Gibt die Einheit zum jeweiligen Wert an
    einheit: Mengeneinheit

    # optional attributes
    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: Optional[datetime] = None
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: Optional[datetime] = None
    _bis_check = field_validator("enddatum")(check_bis_is_later_than_von)

    @staticmethod
    def _get_inclusive_start(values: ValidationInfo) -> Optional[datetime]:
        """a method for easier usage of the check_bis_is_later_than_von validator"""
        return values.data["startdatum"]  # type:ignore[attr-defined]

    # def _get_exclusive_end(self) -> Optional[datetime]:
    #     """a method for easier usage of the check_bis_is_later_than_von validator"""
    #     return self.enddatum
