# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class TechnischeRessourceVerbrauchsart(StrEnum):
    """
    Verbrauchsart der technischen Ressource
    """

    KRAFT_LICHT = "KRAFT_LICHT"
    WAERME = "WAERME"
    E_MOBILITAET = "E_MOBILITAET"
    STRASSENBELEUCHTUNG = "STRASSENBELEUCHTUNG"
