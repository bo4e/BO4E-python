"""
Contains base class for all components
"""
import attr
from marshmallow import Schema

from bo4e.cases import JavaScriptMixin


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class COM:
    """
    abstract base class for all components
    """


class COMSchema(Schema, JavaScriptMixin):
    """
    This is an "abstract" class.
    Inherits from Schema and JavaScriptMixin.
    All components objects are inherited from this class.
    """
