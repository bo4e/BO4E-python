# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class EMobilitaetsart(StrEnum):
    """
    Art der E-Mobilität
    """

    WALLBOX = "WALLBOX"
    E_MOBILITAETSLADESAEULE = "E_MOBILITAETSLADESAEULE"
    LADEPARK = "LADEPARK"
