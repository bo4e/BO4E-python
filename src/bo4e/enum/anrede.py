from enum import Enum


class Anrede(str, Enum):
    """
    Übersicht möglicher Anreden, z.B. eines Geschäftspartners.
    """

    HERR = "HERR"
    FRAU = "FRAU"
    EHELEUTE = "EHELEUTE"
    FIRMA = "FIRMA"
    INDIVIDUELL = "INDIVIDUELL"  # Individuell festgelegt
