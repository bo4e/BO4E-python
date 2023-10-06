"""
contains the COM Zeitmenge
"""
from decimal import Decimal

from bo4e.com.com import COM
from bo4e.enum.zeiteinheit import Zeiteinheit


class Zeitmenge(COM):
    """
    Eine Zeitmenge ist eine Anzahl mit Zeiteinheit; z.B. "5 Tage" oder "1 Monat".
    Der Unterschied zur Zeitspanne ist, dass Start- und Endzeitpunkt nicht angegeben werden.
    Die Zeitmenge ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Zeitmenge aufgeteilt wurde.
    """

    # I made those _not_ optional because the entire instance of Zeitmenge is pointless if one of the two is missing
    einheit: Zeiteinheit  #: z.B. Tage
    dauer: Decimal  #: z.B: 5
