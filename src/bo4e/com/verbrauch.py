"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Optional

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import constr, validator

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
    obis_kennzahl: constr(strict=True, regex=OBIS_PATTERN)  # type: ignore[valid-type]  # type: ignore[valid-type]
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal
    #: Gibt die Einheit zum jeweiligen Wert an
    mengeneinheit: Mengeneinheit

    # optional attributes
    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: Optional[datetime] = None
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: Optional[datetime] = None
    _bis_check = validator("enddatum", always=True, allow_reuse=True)(check_bis_is_later_than_von)

    @staticmethod
    def _get_inclusive_start(values: Dict[str, Any]) -> Optional[datetime]:
        """a method for easier usage of the check_bis_is_later_than_von validator"""
        return values["startdatum"]

    # def _get_exclusive_end(self) -> Optional[datetime]:
    #     """a method for easier usage of the check_bis_is_later_than_von validator"""
    #     return self.enddatum
