"""
Diese Rollen kann ein Geschäftspartner einnehmen.
"""
from enum import Enum

_geschaeftspartnerrolle = {
    "LIEFERANT": "LIEFERANT",
    "DIENSTLEISTER": "DIENSTLEISTER",
    "KUNDE": "KUNDE",
    "INTERESSENT": "INTERESSENT",
    "MARKTPARTNER": "MARKTPARTNER",
}
Geschaeftspartnerrolle = Enum("Geschaeftspartnerrolle", _geschaeftspartnerrolle)
