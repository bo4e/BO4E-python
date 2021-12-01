# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Vertragsstatus(StrEnum):
    """
    Abbildung einer Statusinformation für Verträge.
    """

    IN_ARBEIT = "IN_ARBEIT"  #: in Arbeit
    UEBERMITTELT = "UEBERMITTELT"  #: übermittelt
    ANGENOMMEN = "ANGENOMMEN"  #: angenommen
    AKTIV = "AKTIV"  #: aktiv
    ABGELEHNT = "ABGELEHNT"  #: abgelehnt
    WIDERRUFEN = "WIDERRUFEN"  #: widerrufen
    STORNIERT = "STORNIERT"  #: storniert
    GEKUENDIGT = "GEKUENDIGT"  #: gekündigt
    BEENDET = "BEENDET"  #: beendet
