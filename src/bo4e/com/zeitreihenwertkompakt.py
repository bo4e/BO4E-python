"""
Contains Zeitreihenwertkompakt class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Zeitreihenwertkompakt(COM):
    """
    Abbildung eines kompakten Zeitreihenwertes in dem ausschliesslich der Wert und Statusinformationen stehen.

    .. HINT::
        `Zeitreihenwertkompakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZeitreihenwertkompaktSchema.json>`_

    """

    # required attributes
    wert: Decimal  #: Der im Zeitintervall gültige Wert.

    # optional attributes
    status: Optional[Messwertstatus] = attrs.field(
        default=None
    )  #: Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen.

    statuszusatz: Optional[Messwertstatuszusatz] = attrs.field(
        default=None
    )  #: Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert.


class ZeitreihenwertkompaktSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitreihenwertkompakt.
    """

    class_name = Zeitreihenwertkompakt
    # required attributes
    wert = fields.Decimal(as_string=True)

    # optional attributes
    status = EnumField(Messwertstatus, load_default=None)
    statuszusatz = EnumField(Messwertstatuszusatz, load_default=None)
