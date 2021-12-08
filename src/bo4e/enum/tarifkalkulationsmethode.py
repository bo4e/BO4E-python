# pylint: disable=missing-module-docstring,line-too-long
from bo4e.enum.strenum import StrEnum


class Tarifkalkulationsmethode(StrEnum):
    """
    Auflistung der verschiedenen Berechnungsmethoden für ein Preisblatt.
    """

    KEINE = "KEINE"  #: Es wird keine Berechnung durchgeführt, sondern lediglich die Menge mit dem Preis multipliziert.
    STAFFELN = "STAFFELN"  #: Staffelmodell, d.h. die Gesamtmenge wird in eine Staffel eingeordnet und für die gesamte Menge gilt der so ermittelte Preis
    ZONEN = "ZONEN"  #: Zonenmodell, d.h. die Gesamtmenge wird auf die Zonen aufgeteilt und für die Teilmengen gilt der jeweilige Preis der Zone.
    BESTABRECHNUNG_STAFFEL = "BESTABRECHNUNG_STAFFEL"  #: Bestabrechnung innerhalb der Staffelung
    PAKETPREIS = "PAKETPREIS"  #: Preis für ein Paket (eine Menge).
