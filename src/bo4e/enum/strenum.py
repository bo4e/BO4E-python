"""
strenum contains an enum that inherits from the plain enum and string.
"""

import sys
from enum import Enum

if sys.version_info < (3, 10):
    # pylint: disable=too-few-public-methods
    class StrEnum(str, Enum):
        """
        An enum with string values. This is obsolete for Python >=3.10
        """


else:
    from enum import StrEnum  # pylint: disable=unused-import
