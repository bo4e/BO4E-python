# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Marktrolle(StrEnum):
    """
    Diese Rollen kann ein Marktteilnehmer einnehmen.
    """

    NB = "NB"  #: Grid Operator
    LF = "LF"  #: Supplier
    MSB = "MSB"  #: Messstellenbetreiber
    DL = "DL"  #: Dienstleister
    BKV = "BKV"  #: Bilanzkreisverantwortlicher,
    BKO = "BKO"  #: Bilanzkoordinator / Marktgebietsverantwortlicher
    UENB = "UENB"  #: Übertragungsnetzbetreiber
    KUNDE_SELBST_NN = "KUNDE_SELBST_NN"  #: Kunden, die Netznutzungsentgelte selbst zahlen
    MGV = "MGV"  #: Marktgebietsverantwortlicher
    EIV = "EIV"  #: Einsatzverantwortlicher
    RB = "RB"  #: Registerbetreiber
    KUNDE = "KUNDE"
    INTERESSENT = "INTERESSENT"
    BTR = "BTR"  #: Betreiber einer technischen Ressource
