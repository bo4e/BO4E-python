"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class StandorteigenschaftenGas(COM):
    """
    Standorteigenschaften der Sparte Gas.
    """

    # required attributes
    netzkontonummern: str  #: Netzkontonummern der Gasnetze
    marktgebiete: MarktgebietInfo  #: Die Informationen zu Marktgebieten in dem Netz.


class StandorteigenschaftenGasSchema(COMSchema):
    """
    Schema for de-/serialization of StandorteigenschaftenGas.
    """

    netzkontonummern = fields.Str()
    marktgebiete = fields.Str()

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> StandorteigenschaftenGas:
        """Deserialize JSON to StandorteigenschaftenGas object"""
        return StandorteigenschaftenGas(**data)
