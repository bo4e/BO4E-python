"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from bo4e.validators import check_bis_is_later_than_von, obis_validator


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Verbrauch(COM):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/VerbrauchSchema.json>`_

    """

    # required attributes
    #: Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt
    wertermittlungsverfahren: Wertermittlungsverfahren = attrs.field(
        validator=attrs.validators.instance_of(Wertermittlungsverfahren)
    )
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: str = attrs.field(validator=obis_validator)
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Gibt die Einheit zum jeweiligen Wert an
    mengeneinheit: Mengeneinheit = attrs.field(validator=attrs.validators.instance_of(Mengeneinheit))

    # optional attributes
    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: Optional[datetime] = attrs.field(
        default=None,
        validator=attrs.validators.optional([attrs.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: Optional[datetime] = attrs.field(
        default=None,
        validator=attrs.validators.optional([attrs.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )

    def _get_inclusive_start(self) -> Optional[datetime]:
        """a method for easier usage of the check_bis_is_later_than_von validator"""
        return self.startdatum

    def _get_exclusive_end(self) -> Optional[datetime]:
        """a method for easier usage of the check_bis_is_later_than_von validator"""
        return self.enddatum


class VerbrauchSchema(COMSchema):
    """
    Schema for de-/serialization of Verbrauch
    """

    class_name = Verbrauch
    # required attributes
    wertermittlungsverfahren = EnumField(Wertermittlungsverfahren)
    obis_kennzahl = fields.Str(data_key="obisKennzahl")
    wert = fields.Decimal(as_string=True)
    mengeneinheit = EnumField(Mengeneinheit)

    # optional attributes
    startdatum = fields.DateTime(allow_none=True)
    enddatum = fields.DateTime(allow_none=True)
