# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Vertragsstatus(StrEnum):
    """
    Abbildung einer Statusinformation für Verträge.
    """

    AKTIV = "AKTIV"
    """aktiv; die Beendigung wird über das Vertragsende modelliert"""
    GEKUENDIGT = "GEKUENDIGT"
    """gekündigt"""
    STORNIERT = "STORNIERT"
    """storniert (durch den Vertragsaussteller)"""
    WIDERRUFEN = "WIDERRUFEN"
    """widerrufen (durch den Vertragsempfänger)"""
