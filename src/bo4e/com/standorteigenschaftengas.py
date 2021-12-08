"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema
from bo4e.com.marktgebietinfo import MarktgebietInfo, MarktgebietInfoSchema


# pylint: disable=unused-argument
def check_list_length(instance, attribute, value):
    """
    Check if list length is one or two.
    """
    if len(instance.netzkontonummern) == 0:
        raise ValueError("Netzkontonummern must not be empty.")
    if len(instance.netzkontonummern) > 2:
        raise ValueError("Maximum number of Netzkontonummern is 2.")


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class StandorteigenschaftenGas(COM):
    """
    Standorteigenschaften der Sparte Gas.
    """

    # required attributes
    netzkontonummern: List[str] = attr.ib(validator=check_list_length)  #: Netzkontonummern der Gasnetze
    marktgebiete: List[MarktgebietInfo]  #: Die Informationen zu Marktgebieten in dem Netz.


class StandorteigenschaftenGasSchema(COMSchema):
    """
    Schema for de-/serialization of StandorteigenschaftenGas.
    """

    # required attributes
    netzkontonummern = fields.List(fields.Str())
    marktgebiete = fields.List(fields.Nested(MarktgebietInfoSchema))

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> StandorteigenschaftenGas:
        """Deserialize JSON to StandorteigenschaftenGas object"""
        return StandorteigenschaftenGas(**data)
