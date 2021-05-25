"""
Bei diesem Enum handelt es sich um die Abbildung von Zählertypen der Sparten Strom und Gas.
"""

from enum import Enum

_zaehlertyp = {
    "DREHSTROMZAEHLER": "DREHSTROMZAEHLER",  # Drehstromzähler
    "BALGENGASZAEHLER": "BALGENGASZAEHLER",  # Balgengaszähler
    "DREHKOLBENZAEHLER": "DREHKOLBENZAEHLER",  # Drehkolbengaszähler
    "SMARTMETER": "SMARTMETER",  # Smart Meter Zähler
    "LEISTUNGSZAEHLER": "LEISTUNGSZAEHLER",  # leistungsmessender Zähler
    "MAXIMUMZAEHLER": "MAXIMUMZAEHLER",  # Maximumzähler
    "TURBINENRADGASZAEHLER": "TURBINENRADGASZAEHLER",  # Turbinenradgaszähler
    "ULTRASCHALLGASZAEHLER": "ULTRASCHALLGASZAEHLER",  # Ultraschallgaszähler
    "WECHSELSTROMZAEHLER": "WECHSELSTROMZAEHLER",  # Wechselstromzähler
}
Zaehlertyp = Enum("Zaehlertyp", _zaehlertyp)
