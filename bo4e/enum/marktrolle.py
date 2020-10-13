from enum import Enum


class Marktrolle(str, Enum):
    """
    Diese Rollen kann ein Marktteilnehmer einnehmen.
    """

    VNB = "NB"  # Verteilnetzbetreiber
    LF = "LF"  # Lieferant
    MSB = "MSB"  # metering service operator
    DIENSTLEISTER = "DL"  # unspecified service provider
    BKV = "BKV"  # Bilanzkreisverantwortlicher,
    BIKO = "BKV"  # Bilanzkoordinator / Marktgebietsverantwortlicher
    UENB = "UENB"  # Übertragungsnetzbetreiber
    KUNDE_NN_SELBST = (
        "KUNDE-NN-SELBST"  # Kunden, die Netznutzungsentgelte selbst zahlen
    )
    MGV = "MGV"  # Marktgebietsverantwortlicher
    EIV = "EIV"  # Einsatzverantwortlicher
    RB = "RB"  # Registerbetreiber
    KUNDE = "KUNDE"
    INTERESSENT = "INTERESSENT"
