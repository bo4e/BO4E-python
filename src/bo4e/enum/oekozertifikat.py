# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Oekozertifikat(StrEnum):
    """
    Zertifikate für Ökostrom von verschiedenen Herausgebern.
    """

    CMS_EE01 = "CMS_EE01"  #: CMS_EE01
    CMS_EE02 = "CMS_EE02"  #: CMS_EE02
    EECS = "EECS"  #: EECS
    FRAUNHOFER = "FRAUNHOFER"  #: FRAUNHOFER
    BET = "BET"  #: BET
    KLIMA_INVEST = "KLIMA_INVEST"  #: KLIMA_INVEST
    LGA = "LGA"  #: LGA
    FREIBERG = "FREIBERG"  #: FREIBERG
    RECS = "RECS"  #: RECS
    REGS_EGL = "REGS_EGL"  #: REGS_EGL
    TUEV = "TUEV"  #: TUEV
    TUEV_HESSEN = "TUEV_HESSEN"  #: TUEV_HESSEN
    TUEV_NORD = "TUEV_NORD"  #: TUEV_NORD
    TUEV_RHEINLAND = "TUEV_RHEINLAND"  #: TUEV_RHEINLAND
    TUEV_SUED = "TUEV_SUED"  #: TUEV_SUED
    TUEV_SUED_EE01 = "TUEV_SUED_EE01"  #: TUEV_SUED_EE01
    TUEV_SUED_EE02 = "TUEV_SUED_EE02"  #: TUEV_SUED_EE02
