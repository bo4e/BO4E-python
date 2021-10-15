"""
Abbildung einer Statusinformation für Verträge.
"""
from enum import Enum

Vertragsstatus = Enum(
    "Vertragsstatus",
    {
        "IN_ARBEIT": "IN_ARBEIT",  # in Arbeit
        "UEBERMITTELT": "UEBERMITTELT",  # übermittelt
        "ANGENOMMEN": "ANGENOMMEN",  # angenommen
        "AKTIV": "AKTIV",  # aktiv
        "ABGELEHNT": "ABGELEHNT",  # abgelehnt
        "WIDERRUFEN": "WIDERRUFEN",  # widerrufen
        "STORNIERT": "STORNIERT",  # storniert
        "GEKUENDIGT": "GEKUENDIGT",  # gekündigt
        "BEENDET": "BEENDET",  # beendet
    },
)
