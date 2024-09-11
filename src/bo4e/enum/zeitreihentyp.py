"""
Contains Enums for Zeitreihentyp.
"""

from bo4e.enum.strenum import StrEnum


class Zeitreihentyp(StrEnum):
    """
    Codes der Summenzeitreihentypen.

    Die nachfolgenden Codes sind in DE7111 zu nutzen:
    https://www.edi-energy.de/index.php?id=38&tx_bdew_bdew%5Buid%5D=695&tx_bdew_bdew%5Baction%5D=download
    &tx_bdew_bdew%5Bcontroller%5D=Dokument&cHash=67782e05d8b0f75fbe3a0e1801d07ed0
    """

    EGS = "EGS"  #: Einspeisegangsumme
    LGS = "LGS"  #: Lastgangsumme
    NZR = "NZR"  #: Netzzeitreihe
    SES = "SES"  #: Standardeinspeiseprofilsumme
    SLS = "SLS"  #: Standardlastsumme
    TES = "TES"  #: tagesparameterabhängige Einspeiseprofilsumme
    TLS = "TLS"  #: tagesparameterabhängige Lastprofilsumme
    SLS_TLS = "SLS_TLS"  #: gemeinsame Messung aus SLS und TLS
    SES_TES = "SES_TES"  #: gemeinsame Messung aus SES und TES
