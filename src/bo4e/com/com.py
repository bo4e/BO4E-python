"""
Contains base class for all components
"""

from decimal import Decimal
from typing import Annotated, Optional, Type, TypeVar

from humps.main import camelize

# pylint: disable=no-name-in-module
from pydantic import BaseModel, ConfigDict, Field

from bo4e.version import __version__
from bo4e.zusatzattribut import ZusatzAttribut

# pylint: disable=too-few-public-methods
#
from ..utils import postprocess_docstring


@postprocess_docstring
class COM(BaseModel):
    """
    base class for all components

    .. raw:: html

        <object data="../_static/images/bo4e/com/COM.svg" type="image/svg+xml"></object>

    .. HINT::
        `COM JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/COM.json>`_

    """

    version: Annotated[
        Optional[str], Field(alias="_version")
    ] = __version__  #: Version der BO-Struktur aka "fachliche Versionierung"

    # Python internal: The field is not named '_id' because leading underscores are not allowed in pydantic field names.
    # NameError: Fields must not use names with leading underscores; e.g., use 'id' instead of '_id'.
    id: Annotated[Optional[str], Field(alias="_id")] = None
    """
    Eine generische ID, die für eigene Zwecke genutzt werden kann.
    Z.B. könnten hier UUIDs aus einer Datenbank stehen oder URLs zu einem Backend-System.
    """

    zusatz_attribute: Optional[list[ZusatzAttribut]] = None

    # pylint: disable=duplicate-code
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        extra="allow",
        # json_encoders is deprecated, but there is no easy-to-use alternative. The best way would be to create
        # an annotated version of Decimal, but you would have to use it everywhere in the pydantic models.
        # See this issue for more info: https://github.com/pydantic/pydantic/issues/6375
        json_encoders={Decimal: str},
    )
    """
    basic configuration for pydantic's behaviour
    """


# pylint: disable=invalid-name
#: Any type derived from COM including those that do not directly inherit from COM
TCom = TypeVar("TCom", bound=Type[COM])


# todo: find out if this way of typing is correct
