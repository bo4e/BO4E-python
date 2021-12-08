"""
Contains Zaehlwerk class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attr

from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zeitreihenwertkompakt(COM):
    """
    Abbildung eines kompakten Zeitreihenwertes in dem ausschliesslich der Wert und Statusinformationen stehen.
    """


# Der im Zeitintervall gültige Wert.
wert: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))
# Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen.
status: Messwertstatus
# Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert.
statuszusatz: Messwertstatuszusatz


class ZeitreihenwertkompaktSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitreihenwertkompakt.
    """


wert = fields.Decimal(as_string=True)
status = EnumField(Messwertstatus)
statuszusatz = EnumField(Messwertstatuszusatz)

# pylint: disable=no-self-use, unused-argument


@post_load
def deserialize(self, data, **kwargs) -> Zeitreihenwertkompakt:
    """Deserialize JSON to Zeitreihenwertkompakt object"""
    return Zeitreihenwertkompakt(**data)
