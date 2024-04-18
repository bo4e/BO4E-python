# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Speicherart(StrEnum):
    """ """

    WASSERSTOFFSPEICHER = "WASSERSTOFFSPEICHER"
    PUMPSPEICHER = "PUMPSPEICHER"
    BATTERIESPEICHER = "BATTERIESPEICHER"
    SONSTIGE_SPEICHERART = "SONSTIGE_SPEICHERART"
