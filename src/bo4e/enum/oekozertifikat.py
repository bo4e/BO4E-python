# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Oekozertifikat(StrEnum):
    """
    Zertifikate für Ökostrom von verschiedenen Herausgebern.
    """

    CMS_EE01  #: CMS Standard EEO1
    CMS_EE02  #: CMS Standard EEO2
    EECS  #: EECS
    FRAUNHOFER  #: Fraunhofer Institut
    BET  #: Gutachten von BET Aachen
    KLIMA_INVEST  #: KlimaINVEST
    LGA  #: LGA (Landesgewerbeanstalt Bayern)
    FREIBERG  #: Oeko Institut e.V. Freiburg
    RECS  #: RECS
    REGS_EGL  #: REGS für EGL AG
    TUEV  #: TUEV
    TUEV_HESSEN  #: TUEV Hessen
    TUEV_NORD  #: TUEV Nord
    TUEV_RHEINLAND  #: TUEV Rheinland
    TUEV_SUED  #: TUEV Sued
    TUEV_SUED_EE01  #: TUEV Sued EE01
    TUEV_SUED_EE02  #: TUEV Sued EE02
