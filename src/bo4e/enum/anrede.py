# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Anrede(StrEnum):
    """
    Übersicht möglicher Anreden, z.B. eines Geschäftspartners.
    """

    HERR = "HERR"
    FRAU = "FRAU"
    EHELEUTE = "EHELEUTE"
    FIRMA = "FIRMA"
    INDIVIDUELL = "INDIVIDUELL"
