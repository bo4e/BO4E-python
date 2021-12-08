"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

import attr
from marshmallow import fields, post_load

from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt, ZeitreihenwertkompaktSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zeitreihenwert(Zeitreihenwertkompakt):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.
    """

    # required attributes
    datumUhrzeitVon: datetime = attr.ib(
        validator=attr.validators.instance_of(datetime)
    )  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall begonnen wurde
    datumUhrzeitBis: datetime = attr.ib(
        validator=attr.validators.instance_of(datetime)
    )  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall endet


class ZeitreihenwertSchema(ZeitreihenwertkompaktSchema):
    """
    Schema for de-/serialization of Zeitreihenwert.
    """

    # required attributes
    datumUhrzeitVon = fields.DateTime(load_default=None)
    datumUhrzeitBis = fields.DateTime(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Zeitreihenwert:
        """Deserialize JSON to Zeitreihenwert object"""
        return Zeitreihenwert(**data)
