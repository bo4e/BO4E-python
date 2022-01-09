"""
Contains StandorteigenschaftenGas class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List

import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.marktgebietinfo import MarktgebietInfo, MarktgebietInfoSchema
from bo4e.validators import check_list_length_is_one_or_two


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class StandorteigenschaftenGas(COM):
    """
    Standorteigenschaften der Sparte Gas.
    """

    # required attributes
    netzkontonummern: List[str] = attr.ib(validator=check_list_length_is_one_or_two)  #: Netzkontonummern der Gasnetze
    marktgebiete: List[MarktgebietInfo]  #: Die Informationen zu Marktgebieten in dem Netz.


class StandorteigenschaftenGasSchema(COMSchema):
    """
    Schema for de-/serialization of StandorteigenschaftenGas.
    """

    class_name = StandorteigenschaftenGas
    # required attributes
    netzkontonummern = fields.List(fields.Str())
    marktgebiete = fields.List(fields.Nested(MarktgebietInfoSchema))
