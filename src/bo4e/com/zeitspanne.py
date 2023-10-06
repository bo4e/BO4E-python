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

    # I made those _not_ optional because the entire instance of Zeitmenge is pointless if one of the two is missing
    start: Optional[datetime] = None  #: inklusiver Beginn
    ende: Optional[datetime] = None  #: exklusives Ende
