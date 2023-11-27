"""
contains the COM Zeitspanne
"""
from datetime import datetime
from typing import Optional

from bo4e.com.com import COM


class Zeitspanne(COM):
    """
    Eine Zeitspanne ist definiert aus Start und/oder Ende.
    Der Unterschied zur Menge (die auch zur Abbildung von Zeitmengen genutzt wird) ist, dass konkrete Start- und Endzeitpunkte angegeben werden.
    Die Zeitspanne ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Menge aufgeteilt wurde.
    """

    start: Optional[datetime] = None  #: inklusiver Beginn
    ende: Optional[datetime] = None  #: exklusives Ende
