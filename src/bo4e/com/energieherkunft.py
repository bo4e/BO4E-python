"""
Contains Energieherkunft class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.erzeugungsart import Erzeugungsart


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Energieherkunft(COM):
    """
    Abbildung einer Energieherkunft.
    """

    # required attributes
    #: Art der Erzeugung der Energie.
    erzeugungsart: Erzeugungsart = attr.ib(validator=attr.validators.in_(Erzeugungsart))
    #: Prozentualer Anteil der jeweiligen Erzeugungsart.
    anteil_prozent: Decimal = attr.ib(validator=attr.validators.instance_of(Decimal))

    @anteil_prozent.validator
    # pylint: disable=unused-argument, no-self-use
    def check_percentage_between_0_100(self, attribute, value):
        """Checks that the percentage is between 0 and 100."""
        if not 0 <= value <= 100:
            raise ValueError("anteil_prozent must be between 0 and 100")


class EnergieherkunftSchema(COMSchema):
    """
    Schema for de-/serialization of Energieherkunft.
    """

    # required attributes
    erzeugungsart = EnumField(Erzeugungsart)
    anteil_prozent = fields.Decimal(as_string=True)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Energieherkunft:
        """Deserialize JSON to Energieherkunft object"""
        return Energieherkunft(**data)
