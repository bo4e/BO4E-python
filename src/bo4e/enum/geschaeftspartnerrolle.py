# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Geschaeftspartnerrolle(StrEnum):
    """
    Diese Rollen kann ein Geschäftspartner einnehmen.
    """

    LIEFERANT = "LIEFERANT"
    DIENSTLEISTER = "DIENSTLEISTER"
    KUNDE = "KUNDE"
    INTERESSENT = "INTERESSENT"
    MARKTPARTNER = "MARKTPARTNER"
