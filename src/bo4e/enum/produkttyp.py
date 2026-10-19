# pylint:disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Produkttyp(StrEnum):
    """
    Aufzählung der Produktarten.
    """

    TARIFPRODUKT = "TARIFPRODUKT"
    """Ein Produkt, das auf einem Tarif basiert."""
