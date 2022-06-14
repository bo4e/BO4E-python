"""
Contains Zeitreihenwert class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime


from marshmallow import fields

from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt
from bo4e.validators import check_bis_is_later_than_von


# pylint: disable=too-few-public-methods


class Zeitreihenwert(Zeitreihenwertkompakt):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.

    .. HINT::
        `Zeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZeitreihenwertSchema.json>`_

    """

    # required attributes
    datum_uhrzeit_von: datetime = attrs.field(
        validator=[attrs.validators.instance_of(datetime), check_bis_is_later_than_von]
    )  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall begonnen wurde (inklusiv)
    datum_uhrzeit_bis: datetime = attrs.field(
        validator=[attrs.validators.instance_of(datetime), check_bis_is_later_than_von]
    )  #: Datum Uhrzeit mit Auflösung Sekunden an dem das Messintervall endet (exklusiv)

    def _get_inclusive_start(self) -> datetime:
        """return the inclusive start (used in the validator)"""
        return self.datum_uhrzeit_von

    def _get_exclusive_end(self) -> datetime:
        """return the exclusive end (used in the validator)"""
        return self.datum_uhrzeit_bis
