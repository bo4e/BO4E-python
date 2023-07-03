"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo

from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt
from bo4e.validators import check_bis_is_later_than_von

# pylint: disable=too-few-public-methods


class Zeitreihenwert(Zeitreihenwertkompakt):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitreihenwert.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Zeitreihenwert.json>`_

    """

    # required attributes
    datum_uhrzeit_von: datetime  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall begonnen wurde (inklusiv)
    datum_uhrzeit_bis: datetime  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall endet (exklusiv)
    _bis_check = field_validator("datum_uhrzeit_bis")(check_bis_is_later_than_von)

    @staticmethod
    def _get_inclusive_start(values: ValidationInfo) -> datetime:
        """return the inclusive start (used in the validator)"""
        return values.data["datum_uhrzeit_von"]  # type:ignore[attr-defined]

    # def _get_exclusive_end(self) -> datetime:
    #     """return the exclusive end (used in the validator)"""
    #     return self.datum_uhrzeit_bis
