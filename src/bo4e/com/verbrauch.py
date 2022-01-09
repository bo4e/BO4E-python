"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from bo4e.validators import check_bis_is_later_than_von, obis_validator


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Verbrauch(COM):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs
    """

    # required attributes
    #: Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt
    wertermittlungsverfahren: Wertermittlungsverfahren = attr.ib(
        validator=attr.validators.instance_of(Wertermittlungsverfahren)
    )
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: str = attr.ib(validator=obis_validator)
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Gibt die Einheit zum jeweiligen Wert an
    mengeneinheit: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))

    # optional attributes
    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: Optional[datetime] = attr.ib(
        default=None,
        validator=attr.validators.optional([attr.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: Optional[datetime] = attr.ib(
        default=None,
        validator=attr.validators.optional([attr.validators.instance_of(datetime), check_bis_is_later_than_von]),
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
    obis_kennzahl = fields.Str()
    wert = fields.Decimal(as_string=True)
    mengeneinheit = EnumField(Mengeneinheit)

    # optional attributes
    startdatum = fields.DateTime(allow_none=True)
    enddatum = fields.DateTime(allow_none=True)
