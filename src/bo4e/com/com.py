"""
Contains base class for all components
"""
from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from humps.main import camelize


def to_camel(string):
    return camelize(string)


# pylint: disable=too-few-public-methods
#
class COM(BaseModel):
    """
    base class for all components
    """

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


#: Any type derived from COM including those that do not directly inherit from COM
TCom = TypeVar("TCom", bound=Type[COM])
# todo: find out if this way of typing is correct
