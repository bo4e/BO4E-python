# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Kontaktart(StrEnum):
    """
    Art des Kontaktes zwischen Geschäftspartnern.
    """

    ANSCHREIBEN = "ANSCHREIBEN"
    TELEFONAT = "TELEFONAT"
    FAX = "FAX"
    E_MAIL = "E_MAIL"
    SMS = "SMS"
