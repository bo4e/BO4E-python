"""
Diese Rollen kann ein Marktteilnehmer einnehmen.
"""
from enum import Enum

_marktrolle = {
    "VNB": "NB",  # Grid Operator
    "LF": "LF",  # Supplier
    "MSB": "MSB",  # Messstellenbetreiber
    "DIENSTLEISTER": "DL",  # Dienstleister
    "BKV": "BKV",  # Bilanzkreisverantwortlicher,
    "BIKO": "BKV",  # Bilanzkoordinator / Marktgebietsverantwortlicher
    "UENB": "UENB",  # Übertragungsnetzbetreiber
    "KUNDE_NN_SELBST": "KUNDE-NN-SELBST",  # Kunden, die Netznutzungsentgelte selbst zahlen
    "MGV": "MGV",  # Marktgebietsverantwortlicher
    "EIV": "EIV",  # Einsatzverantwortlicher
    "RB": "RB",  # Registerbetreiber
    "KUNDE": "KUNDE",
    "INTERESSENT": "INTERESSENT",
}
Marktrolle = Enum("Marktrolle", _marktrolle)
