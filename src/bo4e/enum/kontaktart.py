# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Kontaktart(StrEnum):
    """
    Art des Kontaktes zwischen Geschäftspartnern.
    """

    ANSCHREIBEN = "ANSCHREIBEN"  #: Anschreiben
    TELEFONAT = "TELEFONAT"  #: Telefonat
    FAX = "FAX"  #: Fax
    E_MAIL = "E_MAIL"  #: Email
    SMS = "SMS"  #: SMS
