# pylint: disable=missing-module-docstring
from enum import Enum


class Tarifstufen(str, Enum):
    """
    Tarifstufen wie z.B. HT (Hochtarif), NT (Niedertarif), ST (Standardtarif).
    """

    ST = "ST"
    HT = "HT"
    NT = "NT"
