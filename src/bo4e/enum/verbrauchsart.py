"""
Verbrauchsart einer Marktlokation.
"""
from enum import Enum

_verbrauchsart = {
    "KL": "KL",  # Kraft/Licht
    "KLW": "KLW",  # Kraft/Licht/Wärme
    "KLWS": "KLWS",  # Kraft/Licht/Wärme/Speicherheizung
    "W": "W",  # Wärme
    "WS": "WS"  # Wärme/Speicherheizung
}
Verbrauchsart = Enum("Verbrauchsart", _verbrauchsart)
