"""
Contains base class for all components
"""
import attr

# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class COM:
    """
    abstract base class for all components
    """
