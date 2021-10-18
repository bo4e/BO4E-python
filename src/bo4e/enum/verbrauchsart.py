"""
Verbrauchsart einer Marktlokation.
"""
from enum import Enum

Verbrauchsart = Enum(
    "Verbrauchsart",
    {
        "KL": "KL",  # Kraft/Licht
        "KLW": "KLW",  # Kraft/Licht/Wärme
        "KLWS": "KLWS",  # Kraft/Licht/Wärme/Speicherheizung
        "W": "W",  # Wärme
        "WS": "WS",  # Wärme/Speicherheizung
    },
)
