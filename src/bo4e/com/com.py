"""
Contains base class for all components
"""

from decimal import Decimal
from typing import Type, TypeVar

from humps.main import camelize

# pylint: disable=no-name-in-module
from pydantic import BaseModel


# pylint: disable=too-few-public-methods
#
class COM(BaseModel):
    """
    base class for all components

    .. raw:: html

        <object data="../_static/images/bo4e/com/COM.svg" type="image/svg+xml"></object>

    .. HINT::
        `COM JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/COM.json>`_

    """

    class Config:
        """
        basic configuration for pydantic's behaviour
        """

        alias_generator = camelize
        allow_population_by_field_name = True
        json_encoders = {Decimal: str}


#: Any type derived from COM including those that do not directly inherit from COM
TCom = TypeVar("TCom", bound=Type[COM])
# todo: find out if this way of typing is correct
