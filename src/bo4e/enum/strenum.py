"""
strenum contains an enum that inherits from the plain enum and string.
"""

from enum import Enum


# pylint: disable=too-few-public-methods
class StrEnum(str, Enum):
    """
    An enum that has string values.
    """

    # see https://docs.python.org/3/library/enum.html?highlight=strenum#others


# pylint: disable=too-few-public-methods
class DocumentedStrEnum(StrEnum):
    """
    A StrEnum that has docstrings attached to its members.
    """

    # see https://stackoverflow.com/a/50473952/10009545
    def __new__(cls, value, doc=None):
        self = str.__new__(cls, value)  # calling super().__new__(value) here would fail
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self
