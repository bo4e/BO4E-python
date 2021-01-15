"""
Mit dieser Aufzählung kann zwischen den Bilanzierungsmethoden bzw. -grundlagen unterschieden werden.
"""
from enum import Enum

_bilanzierungsmethode = {
    "RLM": "RLM",  # Registrierende Leistungsmessung
    "SLP": "SLP",  # Standard Lastprofil
    "TLP_GEMEINSAM": "TLP_GEMEINSAM",  # TLP gemeinsame Messung
    "TLP_GETRENNT": "TLP_GETRENNT",  # TLP getrennte Messung
    "PAUSCHAL": "PAUSCHAL",  # Pauschale Betrachtung (Band)
}
Bilanzierungsmethode = Enum("Bilanzierungsmethode", _bilanzierungsmethode)
