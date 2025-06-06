# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Oekolabel(StrEnum):
    """
    Aufzählung der Labels für Öko-Strom von verschiedenen Herausgebern.
    """

    ENERGREEN = "ENERGREEN"
    """ENERGREEN"""
    GASGREEN_GRUENER_STROM = "GASGREEN_GRUENER_STROM"
    """GASGREEN_GRUENER_STROM"""
    GASGREEN = "GASGREEN"
    """GASGREEN"""
    GRUENER_STROM_GOLD = "GRUENER_STROM_GOLD"
    """GRUENER_STROM_GOLD"""
    GRUENER_STROM_SILBER = "GRUENER_STROM_SILBER"
    """GRUENER_STROM_SILBER"""
    GRUENER_STROM = "GRUENER_STROM"
    """GRUENER_STROM"""
    GRUENES_GAS = "GRUENES_GAS"
    """GRUENES_GAS"""
    NATURWATT_STROM = "NATURWATT_STROM"
    """NATURWATT_STROM"""
    OK_POWER = "OK_POWER"
    """OK_POWER"""
    RENEWABLE_PLUS = "RENEWABLE_PLUS"
    """RENEWABLE_PLUS"""
    WATERGREEN = "WATERGREEN"
    """WATERGREEN"""
    WATERGREEN_PLUS = "WATERGREEN_PLUS"
    """WATERGREEN_PLUS"""
