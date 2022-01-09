"""
Contains base class for all components
"""
from typing import Type

import attr
from marshmallow import post_load

from bo4e.schemata.caseconverterschema import CaseConverterSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class COM:
    """
    base class for all components
    """


class COMSchema(CaseConverterSchema):
    """
    This is a base class.
    All components objects schemata are inherited from this class.
    """

    #: class_name is needed to use the correct schema for deserialization
    class_name: Type[COM] = COM

    @post_load
    # pylint:disable=unused-argument
    def deserialize(self, data, **kwargs):
        """Deserialize JSON to python object."""
        return type(self).class_name(**data)
