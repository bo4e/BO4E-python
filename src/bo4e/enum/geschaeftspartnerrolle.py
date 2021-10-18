"""
Diese Rollen kann ein Geschäftspartner einnehmen.
"""
from enum import Enum

Geschaeftspartnerrolle = Enum(
    "Geschaeftspartnerrolle",
    {
        "LIEFERANT": "LIEFERANT",
        "DIENSTLEISTER": "DIENSTLEISTER",
        "KUNDE": "KUNDE",
        "INTERESSENT": "INTERESSENT",
        "MARKTPARTNER": "MARKTPARTNER",
    },
)
