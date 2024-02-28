# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Marktrolle(StrEnum):
    """
    Diese Rollen kann ein Marktteilnehmer einnehmen.
    """

    BTR = "BTR"  #: Betreiber einer technischen Ressource
    BIKO = "BIKO"  #: Bilanzkoordinator / Marktgebietsverantwortlicher
    BKV = "BKV"  #: Bilanzkreisverantwortlicher
    DP = "DP"  #: Data Provider
    EIV = "EIV"  #: Einsatzverantwortlicher
    ESA = "ESA"  #: Energieserviceanbieter des Anschlussnutzers
    KN = "KN"  #:  Kapazitätsnutzer
    LF = "LF"  #: Lieferant
    MGV = "MGV"  #: Marktgebietsverantwortlicher
    MSB = "MSB"  #: Messstellenbetreiber
    NB = "NB"  #: Netzbetreiber
    RB = "RB"  #: Registerbetreiber
    UENB = "UENB"  #: Übertragungsnetzbetreiber
