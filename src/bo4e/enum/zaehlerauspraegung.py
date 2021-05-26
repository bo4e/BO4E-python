"""
Gibt an, ob es sich um einen Einrichtungs- oder Zweirichtungszähler handelt.
"""

from enum import Enum

_zaehlerauspraegung = {
    "EINRICHTUNGSZAEHLER": "EINRICHTUNGSZAEHLER",  # Einrichtungszaehler
    "ZWEIRICHTUNGSZAEHLER": "ZWEIRICHTUNGSZAEHLER",  # Zweirichtungszaehler
}
Zaehlerauspraegung = Enum("Zaehlerauspraegung", _zaehlerauspraegung)
