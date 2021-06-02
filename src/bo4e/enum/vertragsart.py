"""
Aufzählung der Vertragsarten.
"""
from enum import Enum

_vertragsart = {
    "ENERGIELIEFERVERTRAG": "ENERGIELIEFERVERTRAG",  # Energieliefervertrag
    "NETZNUTZUNGSVERTRAG": "NETZNUTZUNGSVERTRAG",  # Netznutzungsvertrag
    "BILANZIERUNGSVERTRAG": "BILANZIERUNGSVERTRAG",  # Bilanzierungsvertrag
    "MESSSTELLENBETRIEBSVERTRAG": "MESSSTELLENBETRIEBSVERTRAG",  # Messstellenabetriebsvertrag
    "BUENDELVERTRAG": "BUENDELVERTRAG",  # Bündelvertrag
}
Vertragsart = Enum("Vertragsart", _vertragsart)
