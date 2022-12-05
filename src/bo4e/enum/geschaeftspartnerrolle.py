# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Geschaeftspartnerrolle(StrEnum):
    """
    Diese Rollen kann ein Geschäftspartner einnehmen.
    """

    LIEFERANT = "LIEFERANT"  #: Lieferant
    DIENSTLEISTER = "DIENSTLEISTER"  #: Dienstleister
    KUNDE = "KUNDE"  #: Kunde
    INTERESSENT = "INTERESSENT"  #: Interessent
    MARKTPARTNER = "MARKTPARTNER"  #: Marktpartner
    EINE_NEUE_ROLLE = "EINE_NEUE_ROLLE"  #: Test only, do not merge
