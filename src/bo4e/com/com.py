"""
Contains base class for all components
"""
from decimal import Decimal

from decimal import Decimal
from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from humps.main import camelize


# pylint: disable=too-few-public-methods
#
class COM(BaseModel):
    """
    base class for all components
    """

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
        json_encoders = {Decimal: str}
        use_enum_values = True  # Otherwise the dictionaries by obj.dict() would contain Enum-objects instead of strings


#: Any type derived from COM including those that do not directly inherit from COM
TCom = TypeVar("TCom", bound=Type[COM])
# todo: find out if this way of typing is correct
