"""
Art des Kontaktes zwischen Geschäftspartnern.
"""
from enum import Enum

_kontaktart = {
    "ANSCHREIBEN": "ANSCHREIBEN",
    "TELEFONAT": "TELEFONAT",
    "FAX": "FAX",
    "E_MAIL": "E_MAIL",
    "SMS": "SMS",
}
Kontaktart = Enum("Kontaktart", _kontaktart)
