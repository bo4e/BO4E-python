"""
Abbildung verschiedener Rufnummerntypen.
"""

from enum import Enum

_rufnummernart = {
    "RUF_ZENTRALE": "RUF_ZENTRALE",  # Rufnummer Zentrale
    "FAX_ZENTRALE": "FAX_ZENTRALE",  # Faxnummer Zentrale
    "SAMMELRUF": "SAMMELRUF",  # Sammelrufnummer
    "SAMMELFAX": "SAMMELFAX",  # Sammelfaxnummer
    "ABTEILUNGRUF": "ABTEILUNGRUF",  # Rufnummer Abteilung
    "ABTEILUNGFAX": "ABTEILUNGFAX",  # Faxnummer Abteilung
    "RUF_DURCHWAHL": "RUF_DURCHWAHL",  # Rufnummer Durchwahl
    "FAX_DURCHWAHL": "FAX_DURCHWAHL",  # Faxnummer Durchwahl
    "MOBIL_NUMMER": "MOBIL_NUMMER",  # Nummer des mobilen Telefons
}
Rufnummernart = Enum("Rufnummernart", _rufnummernart)
