# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Organisationstyp(StrEnum):
    """
    Hier wird festgelegt, ob der Geschäftspartner eine Person, eine Firma oder etwas anderes ist.
    """

    PRIVATPERSON = "PRIVATPERSON"  #: B2C
    UNTERNEHMEN = "UNTERNEHMEN"  #: B2B
    KOMMUNALE_EINRICHTUNG = "KOMMUNALE_EINRICHTUNG"  #: B2A
    STAATLICHE_BEHOERDE = "STAATLICHE_BEHOERDE"  #: B2G
