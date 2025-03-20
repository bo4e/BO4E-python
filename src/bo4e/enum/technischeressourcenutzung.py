# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class TechnischeRessourceNutzung(StrEnum):
    """
    Nutzung der technischen Ressource
    """

    STROMVERBRAUCHSART = "STROMVERBRAUCHSART"
    STROMERZEUGUNGSART = "STROMERZEUGUNGSART"
    SPEICHER = "SPEICHER"
