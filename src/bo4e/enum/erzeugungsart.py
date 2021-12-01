# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Erzeugungsart(StrEnum):
    """
    Auflistung der Erzeugungsarten von Energie.
    """

    FOSSIL = "FOSSIL"  #: Fossile Brennstoffe
    KWK = "KWK"  #: Kraft-Waerme-Koppelung
    WIND = "WIND"  #: Windkraft
    SOLAR = "SOLAR"  #: Solarenergie
    KERNKRAFT = "KERNKRAFT"  #: Kernkraft
    WASSER = "WASSER"  #: Wasserkraft
    GEOTHERMIE = "GEOTHERMIE"  #: Geothermie
    BIOMASSE = "BIOMASSE"  #: Biomasse
    KOHLE = "KOHLE"  #: Kohle
    GAS = "GAS"  #: Erdgas
    SONSTIGE = "SONSTIGE"  #: Sonstige
    SONSTIGE_EEG = "SONSTIGE_EEG"  #: Sonstige nach EEG
    BIOGAS = "BIOGAS"  #: Biogas
    KLIMANEUTRALES_GAS = "KLIMANEUTRALES_GAS"  #: Klimaneutrales Erdgas
