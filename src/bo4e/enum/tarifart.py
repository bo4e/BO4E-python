"""
Die Tarifart wird verwendet zur Charakterisierung von Zählern und daraus resultierenden Tarifen.
"""

from enum import Enum

_tarifart = {
    "EINTARIF": "EINTARIF",  # Eintarif
    "ZWEITARIF": "ZWEITARIF",  # Zweitarif
    "MEHRTARIF": "MEHRTARIF",  # Mehrtarif
    "SMART_METER": "SMART_METER",  # Smart Meter Tarif
    "LEISTUNGSGEMESSEN": "LEISTUNGSGEMESSEN",  # Leistungsgemessener Tarif
}
Tarifart = Enum("Tarifart", _tarifart)
