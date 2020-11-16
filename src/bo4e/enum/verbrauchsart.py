from enum import Enum


class Verbrauchsart(str, Enum):
    """
    Verbrauchsart einer Marktlokation.
    """

    KL = "KL"  # Kraft/Licht
    KLW = "KLW"  # Kraft/Licht/Wärme
    KLWS = "KLWS"  # Kraft/Licht/Wärme/Speicherheizung
    W = "W"  # Wärme
    WS = "WS"  # Wärme/Speicherheizung
