from enum import Enum


class Bilanzierungsmethode(str, Enum):
    """
    Mit dieser Aufzählung kann zwischen den Bilanzierungsmethoden bzw. -Grundlagen unterschieden werden.
    """

    RLM = "RLM"  # Registrierende Leistungsmessung
    SLP = "SLP"  # Standard Lastprofil
    TLP_GEMEINSAM = "TLP_GEMEINSAM"  # TLP gemeinsame Messung
    TLP_GETRENNT = "TLP_GETRENNT"  # TLP getrennte Messung
    PAUSCHAL = "PAUSCHAL"  # Pauschale Betrachtung (Band)
