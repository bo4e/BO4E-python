# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Anrede(StrEnum):
    """
    Übersicht möglicher Anreden, z.B. eines Geschäftspartners.
    """

    HERR = "HERR"  #: "Herr
    FRAU = "FRAU"  #: Frau
    EHELEUTE = "EHELEUTE"  #: Eheleute
    FIRMA = "FIRMA"  #: Firma
    INDIVIDUELL = "INDIVIDUELL"  #: Individuell (z.B. "Profx")
