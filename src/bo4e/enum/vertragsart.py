"""
Aufzählung der Vertragsarten.
"""
from enum import Enum

Vertragsart = Enum(
    "Vertragsart",
    {
        "ENERGIELIEFERVERTRAG": "ENERGIELIEFERVERTRAG",  # Energieliefervertrag
        "NETZNUTZUNGSVERTRAG": "NETZNUTZUNGSVERTRAG",  # Netznutzungsvertrag
        "BILANZIERUNGSVERTRAG": "BILANZIERUNGSVERTRAG",  # Bilanzierungsvertrag
        "MESSSTELLENBETRIEBSVERTRAG": "MESSSTELLENBETRIEBSVERTRAG",  # Messstellenabetriebsvertrag
        "BUENDELVERTRAG": "BUENDELVERTRAG",  # Bündelvertrag
    },
)
