# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Kontaktart(StrEnum):
    """
    Gibt an, auf welchem Weg die Person oder der Geschäftspartner kontaktiert werden kann.
    """

    POSTWEG = "POSTWEG"  #: Postweg
    TELEFON = "TELEFON"  #: Telefon
    FAX = "FAX"  #: Fax
    E_MAIL = "E_MAIL"  #: E-Mail
    SMS = "SMS"  #: SMS
