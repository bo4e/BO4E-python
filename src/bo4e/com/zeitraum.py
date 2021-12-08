"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
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
@attr.s(auto_attribs=True, kw_only=True)
class Zeitraum(COM):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)
    """

    # optional attributes
    einheit: Optional[Zeiteinheit] = attr.ib(default=None, validator=time_range_possibilities)
    dauer: Optional[Decimal] = attr.ib(default=None, validator=time_range_possibilities)
    startdatum: Optional[datetime] = attr.ib(default=None, validator=time_range_possibilities)
    enddatum: Optional[datetime] = attr.ib(default=None, validator=time_range_possibilities)
    startzeitpunkt: Optional[datetime] = attr.ib(default=None, validator=time_range_possibilities)
    endzeitpunkt: Optional[datetime] = attr.ib(default=None, validator=time_range_possibilities)


class ZeitraumSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitraum.
    """

    # optional attributes
    einheit = EnumField(Zeiteinheit, load_default=None)
    dauer = fields.Decimal(load_default=None, as_string=True)
    startdatum = fields.DateTime(load_default=None)
    enddatum = fields.DateTime(load_default=None)
    startzeitpunkt = fields.DateTime(load_default=None)
    endzeitpunkt = fields.DateTime(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Zeitraum:
        """Deserialize JSON to Zeitraum object"""
        return Zeitraum(**data)
