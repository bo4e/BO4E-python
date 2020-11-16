from enum import Enum


class Kontaktart(str, Enum):
    """
    Art des Kontaktes zwischen Geschäftspartnern.
    """

    ANSCHREIBEN = "ANSCHREIBEN"
    TELEFONAT = "TELEFONAT"
    FAX = "FAX"
    E_MAIL = "E_MAIL"
    SMS = "SMS"
