"""
Contains StandorteigenschaftenStrom class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class StandorteigenschaftenStrom(COM):
    """
    Standorteigenschaften der Sparte Strom
    """

    # required attributes
    #: Die EIC-Nummer des Bilanzierungsgebietes
    bilanzierungsgebiet_eic: str = attr.ib(validator=attr.validators.instance_of(str))
    # todo: use EIC validation: https://github.com/Hochfrequenz/BO4E-python/issues/147

    #: Der Name der Regelzone
    regelzone: str = attr.ib(validator=attr.validators.instance_of(str))

    #: De EIC-Nummer der Regelzone
    regelzone_eic: str = attr.ib(validator=attr.validators.instance_of(str))
    # todo: use EIC validation: https://github.com/Hochfrequenz/BO4E-python/issues/147


class StandorteigenschaftenStromSchema(COMSchema):
    """
    Schema for de-/serialization of StandorteigenschaftenStrom.
    """

    # required attributes
    bilanzierungsgebiet_eic = fields.Str()
    regelzone = fields.Str()
    regelzone_eic = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> StandorteigenschaftenStrom:
        """Deserialize JSON to StandorteigenschaftenGas object"""
        return StandorteigenschaftenStrom(**data)
