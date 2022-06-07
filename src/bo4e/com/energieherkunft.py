"""
Contains Energieherkunft class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.erzeugungsart import Erzeugungsart


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Energieherkunft(COM):
    """
    Abbildung einer Energieherkunft

    .. HINT::
        `Energieherkunft JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/EnergieherkunftSchema.json>`_

    """

    # required attributes
    #: Art der Erzeugung der Energie.
    erzeugungsart: Erzeugungsart = attrs.field(validator=attrs.validators.in_(Erzeugungsart))
    #: Prozentualer Anteil der jeweiligen Erzeugungsart.
    anteil_prozent: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))

    @anteil_prozent.validator
    # pylint: disable=unused-argument
    def check_percentage_between_0_100(self, attribute, value):
        """Checks that the percentage is between 0 and 100."""
        if not 0 <= value <= 100:
            raise ValueError("anteil_prozent must be between 0 and 100")


class EnergieherkunftSchema(COMSchema):
    """
    Schema for de-/serialization of Energieherkunft.
    """

    class_name = Energieherkunft
    # required attributes
    erzeugungsart = EnumField(Erzeugungsart)
    anteil_prozent = fields.Decimal(as_string=True, data_key="anteilProzent")
