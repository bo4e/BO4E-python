"""
Contains base class for all components
"""

from decimal import Decimal
from typing import Type, TypeVar

from humps.main import camelize

# pylint: disable=no-name-in-module
from pydantic import BaseModel, ConfigDict


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

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},  # type: ignore[typeddict-unknown-key]
    )
    """
    basic configuration for pydantic's behaviour
    """


# pylint: disable=invalid-name
#: Any type derived from COM including those that do not directly inherit from COM
TCom = TypeVar("TCom", bound=Type[COM])


# todo: find out if this way of typing is correct
