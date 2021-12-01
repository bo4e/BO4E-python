# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Bilanzierungsmethode(StrEnum):
    """
    Mit dieser Aufzählung kann zwischen den Bilanzierungsmethoden bzw. -grundlagen unterschieden werden.
    """

    RLM = "RLM"  #: Registrierende Leistungsmessung
    SLP = "SLP"  #: Standard Lastprofil
    TLP_GEMEINSAM = "TLP_GEMEINSAM"  #: TLP gemeinsame Messung
    TLP_GETRENNT = "TLP_GETRENNT"  #: TLP getrennte Messung
    PAUSCHAL = "PAUSCHAL"  #: Pauschale Betrachtung (Band)
