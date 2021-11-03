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
