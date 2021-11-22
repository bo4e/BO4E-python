# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Zaehlerauspraegung(StrEnum):
    """
    Gibt an, ob es sich um einen Einrichtungs- oder Zweirichtungszähler handelt.
    """

    EINRICHTUNGSZAEHLER = "EINRICHTUNGSZAEHLER"  #: Einrichtungszaehler
    ZWEIRICHTUNGSZAEHLER = "ZWEIRICHTUNGSZAEHLER"  #: Zweirichtungszaehler
