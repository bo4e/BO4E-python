# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Oekolabel(StrEnum):
    """
    Aufzählung der Labels für Öko-Strom von verschiedenen Herausgebern.
    """

    ENERGREEN  #: energreen
    GASGREEN_GRUENER_STROM  #: energreen (durch Gruener Strom Label)
    GASGREEN  #: gasgreen
    GRUENER_STROM_GOLD  #: Gruener Strom Label Gold
    GRUENER_STROM_SILBER  #: Gruener Strom Label Silber
    GRUENER_STROM  #: Gruener Strom Label
    GRUENES_GAS  #: Gruenes Gas Label
    NATURWATT_STROM  #: NaturWatt Strom
    OK_POWER  #: ok-Power
    RENEWABLE_PLUS  #: RenewablePLUS
    WATERGREEN  #: Watergreen
    WATERGREEN_PLUS  #: Watergreen+
