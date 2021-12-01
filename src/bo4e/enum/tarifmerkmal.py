# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tarifmerkmal(StrEnum):
    """
    Produktmerkmale im Zusammenhang mit der Tarifdefinition.
    """

    STANDARD  #: Standardprodukt
    VORKASSE  #: Vorkassenprodukt
    PAKET  #: Paketpreisprodukt
    KOMBI  #: Kombiprodukt
    FESTPREIS  #: Festpreisprodukt
    BAUSTROM  #: Baustromprodukt
    HAUSLICHT  #: Hauslichtprodukt
    HEIZSTROM  #: Heizstromprodukt
    ONLINE  #: Onlineprodukt
