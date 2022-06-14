"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional


from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from bo4e.validators import check_bis_is_later_than_von, OBIS_PATTERN


# pylint: disable=too-few-public-methods
from pydantic import constr


class Verbrauch(COM):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/VerbrauchSchema.json>`_

    """

    # required attributes
    #: Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt
    wertermittlungsverfahren: Wertermittlungsverfahren
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:
    obis_kennzahl: constr(regex=OBIS_PATTERN)
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal
    #: Gibt die Einheit zum jeweiligen Wert an
    mengeneinheit: Mengeneinheit

    # optional attributes
    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: datetime = attrs.field(
        default=None,
        validator=attrs.validators.optional([attrs.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: datetime = attrs.field(
        default=None,
        validator=attrs.validators.optional([attrs.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )

    def _get_inclusive_start(self) -> Optional[datetime]:
        """a method for easier usage of the check_bis_is_later_than_von validator"""
        return self.startdatum

    def _get_exclusive_end(self) -> Optional[datetime]:
        """a method for easier usage of the check_bis_is_later_than_von validator"""
        return self.enddatum
