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
    Use it like this:
    class MyDocumentedEnum(DocumentedStrEnum):
    Foo = "Serialized Foo", "my good docstring of Foo"
    Bar = "Serialized Bar", "bar is not foo (this is a docstring)"
    Then wherever MyDocumentedEnum is used in BOs or COMs, the attribute will serialize as either "Serialized Foo"
    or "Serialized Bar". And inspect.getdocs(MyDocumentedEnum.Foo) will return the respective docstring.
    This is unittested.
    """

    # see https://stackoverflow.com/a/50473952/10009545
    def __new__(cls, value, doc=None):
        self = str.__new__(cls, value)  # calling super().__new__(value) here would fail
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self
