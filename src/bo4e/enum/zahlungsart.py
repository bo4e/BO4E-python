# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Zahlungsart(StrEnum):
    """
    Gibt an, um was für eine Zahlungsart es sich handelt.
    """

    SEPA_LASTSCHRIFT = "SEPA_LASTSCHRIFT"
    UEBERWEISUNG = "UEBERWEISUNG"
