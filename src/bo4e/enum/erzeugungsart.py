# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Erzeugungsart(StrEnum):
    """
    Auflistung der Erzeugungsarten von Energie.
    """

    FOSSIL  #: Fossile Brennstoffe
    KWK  #: Kraft-Waerme-Koppelung
    WIND  #: Windkraft
    SOLAR  #: Solarenergie
    KERNKRAFT  #: Kernkraft
    WASSER  #: Wasserkraft
    GEOTHERMIE  #: Geothermie
    BIOMASSE  #: Biomasse
    KOHLE  #: Kohle
    GAS  #: Erdgas
    SONSTIGE  #: Sonstige
    SONSTIGE_EEG  #: Sonstige nach EEG
    BIOGAS  #: Biogas
    KLIMANEUTRALES_GAS  #: Klimaneutrales Erdgas
