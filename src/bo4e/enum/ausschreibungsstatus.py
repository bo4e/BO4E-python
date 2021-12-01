# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Ausschreibungsstatus(StrEnum):
    """
    Bezeichnungen für die Ausschreibungsphasen
    """

    PHASE1  #: Phase1: Teilnahmewettbewerb
    PHASE2  #: Phase2: Angebotsphase
    PHASE3  #: Phase3: Verhandlungsphase
    PHASE4  #: Phase4: Zuschlagserteilung
