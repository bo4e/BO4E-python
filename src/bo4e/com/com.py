"""
Contains base class for all components
"""
from typing import Generic, Type, TypeVar

import attr
from marshmallow import post_load

from bo4e.schemata.caseconverterschema import CaseConverterSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class COM:
    """
    base class for all components
    """


#: Any type derived from COM including those that do not directly inherit from COM
TCom = TypeVar("TCom", bound=Type[COM])
# todo: find out if this way of typing is correct


class COMSchema(CaseConverterSchema, Generic[TCom]):
    """
    This is a base class.
    All components objects schemata are inherited from this class.
    """

    #: class_name is needed to use the correct schema for deserialization
    class_name: TCom

    @post_load
    # pylint:disable=unused-argument
    def deserialize(self, data, **kwargs) -> TCom:
        """Deserialize JSON to python object."""
        return type(self).class_name(**data)  # type:ignore[return-value,call-arg]
