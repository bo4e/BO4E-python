# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Steuerkennzeichen(StrEnum):
    """
    Zur Kennzeichnung verschiedener Steuersätze und Verfahren.
    """

    UST_0 = "UST_0"  #: Keine Umsatzsteuer, bzw. nicht steuerbar.
    UST_19 = "UST_19"  #: Umsatzsteuer 19%
    UST_7 = "UST_7"  #: Umsatzsteuer 7%
    VST_0 = "VST_0"  #: Keine Vorsteuer, bzw. nicht steuerbar.
    VST_19 = "VST_19"  #: Vorsteuer 19%
    VST_7 = "VST_7"  #: Vorsteuer 7%
    RCV = "RCV"  #: Reverse Charge Verfahren (Umkehrung der Steuerpflicht)
