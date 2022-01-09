"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

import attr
from marshmallow import fields

from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt, ZeitreihenwertkompaktSchema
from bo4e.validators import check_bis_is_later_than_von


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zeitreihenwert(Zeitreihenwertkompakt):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.
    """

    # required attributes
    datum_uhrzeit_von: datetime = attr.ib(
        validator=[attr.validators.instance_of(datetime), check_bis_is_later_than_von]
    )  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall begonnen wurde (inklusiv)
    datum_uhrzeit_bis: datetime = attr.ib(
        validator=[attr.validators.instance_of(datetime), check_bis_is_later_than_von]
    )  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall endet (exklusiv)

    def _get_inclusive_start(self) -> datetime:
        """return the inclusive start (used in the validator)"""
        return self.datum_uhrzeit_von

    def _get_exclusive_end(self) -> datetime:
        """return the exclusive end (used in the validator)"""
        return self.datum_uhrzeit_bis


class ZeitreihenwertSchema(ZeitreihenwertkompaktSchema):
    """
    Schema for de-/serialization of Zeitreihenwert.
    """

    class_name = Zeitreihenwert  # type:ignore[assignment]
    # required attributes
    datum_uhrzeit_von = fields.DateTime()
    datum_uhrzeit_bis = fields.DateTime()
