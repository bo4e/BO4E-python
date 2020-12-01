from enum import Enum
from iso3166 import countries

"""
Der ISO-Landescode als Enumeration.
"""

alpha2codes = {c.alpha2: c.alpha2 for c in countries}

Landescode = Enum("Landescode", alpha2codes)
