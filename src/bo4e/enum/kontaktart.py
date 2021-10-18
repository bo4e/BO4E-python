"""
Art des Kontaktes zwischen Geschäftspartnern.
"""
from enum import Enum

Kontaktart = Enum(
    "Kontaktart",
    {
        "ANSCHREIBEN": "ANSCHREIBEN",
        "TELEFONAT": "TELEFONAT",
        "FAX": "FAX",
        "E_MAIL": "E_MAIL",
        "SMS": "SMS",
    },
)
