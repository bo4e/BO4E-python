from enum import Enum


class Geschaeftspartnerrolle(str, Enum):
    """
    Diese Rollen kann ein Geschäftspartner einnehmen.
    """

    LIEFERANT = "LIEFERANT"
    DIENSTLEISTER = "DIENSTLEISTER"
    KUNDE = "KUNDE"
    INTERESSENT = "INTERESSENT"
    MARKTPARTNER = "MARKTPARTNER"
