"""
Gibt an, ob es sich um einen Einrichtungs- oder Zweirichtungszähler handelt.
"""

from enum import Enum

Zaehlerauspraegung = Enum(
    "Zaehlerauspraegung",
    {
        "EINRICHTUNGSZAEHLER": "EINRICHTUNGSZAEHLER",  # Einrichtungszaehler
        "ZWEIRICHTUNGSZAEHLER": "ZWEIRICHTUNGSZAEHLER",  # Zweirichtungszaehler
    },
)
