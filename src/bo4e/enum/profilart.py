"""
Contains Enums for Profilart.
"""

from bo4e.enum.strenum import StrEnum


class Profilart(StrEnum):
    """
    Profilart: temperaturabh./Standardlastprofil.
    """

    ART_STANDARDLASTPROFIL = "ART_STANDARDLASTPROFIL"  #: ART_STANDARDLASTPROFIL, Z02
    ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL = "ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL"
    #: ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL, Z03
    ART_LASTPROFIL = "ART_LASTPROFIL"  #: ART_LASTPROFIL, Z12
