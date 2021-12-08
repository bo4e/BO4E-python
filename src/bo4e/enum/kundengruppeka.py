# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class KundengruppeKA(StrEnum):
    """
    Eine Aufzählung zur Einordnung für die Höhe der Konzessionsabgabe.
    """

    S_SCHWACHLAST = "S_SCHWACHLAST"  #: Strom
    S_TARIF_25000 = "S_TARIF_25000"  #: Strom
    S_TARIF_100000 = "S_TARIF_100000"  #: Strom
    S_TARIF_500000 = "S_TARIF_500000"  #: Strom
    S_TARIF_G_500000 = "S_TARIF_G_500000"  #: Strom
    S_SONDERKUNDE = "S_SONDERKUNDE"  #: Strom
    G_KOWA_25000 = "G_KOWA_25000"  #: Gas
    G_KOWA_100000 = "G_KOWA_100000"  #: Gas
    G_KOWA_500000 = "G_KOWA_500000"  #: Gas
    G_KOWA_G_500000 = "G_KOWA_G_500000"  #: Gas
    G_TARIF_25000 = "G_TARIF_25000"  #: Gas
    G_TARIF_100000 = "G_TARIF_100000"  #: Gas
    G_TARIF_500000 = "G_TARIF_500000"  #: Gas
    G_TARIF_G_500000 = "G_TARIF_G_500000"  #: Gas
    G_SONDERKUNDE = "G_SONDERKUNDE"  #: Gas
    SONDER_KAS = "SONDER_KAS"  #: beides
    SONDER_SAS = "SONDER_SAS"  #: beides
    SONDER_TAS = "SONDER_TAS"  #: beides
    SONDER_TKS = "SONDER_TKS"  #: Gas
    SONDER_TSS = "SONDER_TSS"  #: Strom
