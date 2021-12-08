# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Tarifmerkmal(StrEnum):
    """
    Produktmerkmale im Zusammenhang mit der Tarifdefinition.
    """

    STANDARD = "STANDARD"  #: Standardprodukt
    VORKASSE = "VORKASSE"  #: Vorkassenprodukt
    PAKET = "PAKET"  #: Paketpreisprodukt
    KOMBI = "KOMBI"  #: Kombiprodukt
    FESTPREIS = "FESTPREIS"  #: Festpreisprodukt
    BAUSTROM = "BAUSTROM"  #: Baustromprodukt
    HAUSLICHT = "HAUSLICHT"  #: Hauslichtprodukt
    HEIZSTROM = "HEIZSTROM"  #: Heizstromprodukt
    ONLINE = "ONLINE"  #: Onlineprodukt
