"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Protocol

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren

# pylint:disable=line-too-long
OBIS_PATTERN = r"((1)-((?:[0-5]?[0-9])|(?:6[0-5])):((?:[1-8]|99))\.((?:6|8|9|29))\.([0-9]{1,2})|(7)-((?:[0-5]?[0-9])|(?:6[0-5])):(.{1,2})\.(.{1,2})\.([0-9]{1,2}))"


# pylint:disable=too-few-public-methods
class _StartEndType(Protocol):
    """
    an overengineered protocol class
    """

    startdatum: datetime
    enddatum: datetime


# pylint: disable=unused-argument
def check_end_is_later_than_start(instance: _StartEndType, attribute, value):
    """
    assert that bis is later than von
    """
    if not instance.enddatum >= instance.startdatum:
        raise ValueError("enddatum has to be >= startdatum")


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Verbrauch(COM):
    """
    Gibt die Staffelgrenzen der jeweiligen Preise an
    """

    # required attributes
    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: datetime = attr.ib(validator=[attr.validators.instance_of(datetime), check_end_is_later_than_start])
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: datetime = attr.ib(validator=[attr.validators.instance_of(datetime), check_end_is_later_than_start])
    #: Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt
    wertermittlungsverfahren: Wertermittlungsverfahren = attr.ib(
        validator=attr.validators.instance_of(Wertermittlungsverfahren)
    )
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: str = attr.ib(validator=attr.validators.matches_re(regex=OBIS_PATTERN))
    #: Gibt den absoluten Wert der Menge an
    wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
    #: Gibt die Einheit zum jeweiligen Wert an
    mengeneinheit: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))


class VerbauchSchema(COMSchema):
    """
    Schema for de-/serialization of Verbrauch
    """

    # required attributes
    startdatum = fields.DateTime()
    enddatum = fields.DateTime()
    wertermittlungsverfahren = EnumField(Wertermittlungsverfahren)
    obis_kennzahl = fields.Str()
    wert = fields.Decimal()
    mengeneinheit = EnumField(Mengeneinheit)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Verbrauch:
        """Deserialize JSON to Verbrauch object"""
        return Verbrauch(**data)
