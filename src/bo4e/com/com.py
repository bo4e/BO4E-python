"""
Contains base class for all components
"""
import attr

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
