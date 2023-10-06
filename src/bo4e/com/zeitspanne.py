"""
contains the COM Zeitspanne
"""
from datetime import datetime
from typing import Optional

from bo4e.com.com import COM


class Zeitspanne(COM):
    """
    Eine Zeitspanne ist definiert aus Start und/oder Ende.
    Der Unterschied zur Zeitmenge ist, dass konkrete Start- und Endzeitpunkt angegeben werden.
    Die Zeitspanne ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Zeitmenge aufgeteilt wurde.
    """

    start: Optional[datetime] = None  #: inklusiver Beginn
    ende: Optional[datetime] = None  #: exklusives Ende
