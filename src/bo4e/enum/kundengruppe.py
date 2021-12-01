# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Kundengruppe(StrEnum):
    """
    Kundengruppe für eine Marktlokation (orientiert sich an den Standard-Lastprofilen).
    """

    RLM  #: Strom/Gas
    RLM_KOMMUNAL  #: Strom/Gas
    SLP_KOMMUNAL  #: Strom/Gas
    SLP_S_G0  #: Strom
    SLP_S_G1  #: Strom
    SLP_S_G2  #: Strom
    SLP_S_G3  #: Strom
    SLP_S_G4  #: Strom
    SLP_S_G5  #: Strom
    SLP_S_G6  #: Strom
    SLP_S_G7  #: Strom
    SLP_S_L0  #: Strom
    SLP_S_L1  #: Strom
    SLP_S_L2  #: Strom
    SLP_S_H0  #: Strom
    SLP_S_SB  #: Strom
    SLP_S_HZ  #: Strom
    SLP_S_WP  #: Strom
    SLP_S_EM  #: Strom
    SLP_S_HZ_GEM  #: Strom
    SLP_G_GKO  #: Gas
    SLP_G_STANDARD  #: Gas
    SLP_G_GHA  #: Gas
    SLP_G_GMK  #: Gas
    SLP_G_GBD  #: Gas
    SLP_G_GGA  #: Gas
    SLP_G_GBH  #: Gas
    SLP_G_GBA  #: Gas
    SLP_G_GWA  #: Gas
    SLP_G_GGB  #: Gas
    SLP_G_GPD  #: Gas
    SLP_G_GMF  #: Gas
    SLP_G_HEF  #: Gas
    SLP_G_HMF  #: Gas
    SLP_G_HKO  #: Gas
