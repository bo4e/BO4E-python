# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Wertermittlungsverfahren(StrEnum):
    """
    Gibt an, ob es sich um eine Prognose oder eine Messung handelt, beispielsweise bei der Abbildung eines Verbrauchs.
    """

    PROGNOSE = "PROGNOSE"  #: Prognose
    MESSUNG = "MESSUNG"  #: Messung
