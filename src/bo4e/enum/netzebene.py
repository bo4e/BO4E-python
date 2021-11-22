# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Netzebene(StrEnum):
    """
    Auflistung möglicher Netzebenen innerhalb der Energiearten Strom und Gas.
    """

    NSP = "NSP"  #: Niederspannung; Strom
    MSP = "MSP"  #: Mittelspannung; Strom
    HSP = "HSP"  #: Hochspannung; Strom
    HSS = "HSS"  #: Hoechstspannung; Strom
    MSP_NSP_UMSP = "MSP_NSP_UMSP"  #: MS/NS Umspannung; Strom
    HSP_MSP_UMSP = "HSP_MSP_UMSP"  #: HS/MS Umspannung; Strom
    HSS_HSP_UMSP = "HSS_HSP_UMSP"  #: HOES/HS Umspannung; Strom
    HD = "HD"  #: Hochdruck; Gas
    MD = "MD"  #: Mitteldruck; Gas
    ND = "ND"  #: Niederdruck; Gas
