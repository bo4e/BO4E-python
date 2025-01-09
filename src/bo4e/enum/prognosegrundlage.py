"""
Contains Enums for Prognosegrundlage.
"""

from bo4e.enum.strenum import StrEnum


class Prognosegrundlage(StrEnum):
    """
    Prognosegrundlage (WERTE, PROFILE).
    """

    WERTE = "WERTE"  #: Prognose auf Basis von Werten
    PROFILE = "PROFILE"  #: Prognose auf Basis von Profilen
