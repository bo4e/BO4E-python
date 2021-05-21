"""
Contains base class for all components
"""
import attr
from bo4e.cases import JavaScriptMixin
from marshmallow import Schema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class COM:
    """
    base class for all components
    """


class COMSchema(Schema, JavaScriptMixin):
    """
    This is a base class.
    All components objects are inherited from this class.
    """
