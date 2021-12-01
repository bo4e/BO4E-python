# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Rechnungstyp(StrEnum):
    """
    Abbildung verschiedener Rechnungstypen zur Kennzeichnung von Rechnungen
    """

    ENDKUNDENRECHNUNG  #: Eine Rechnung vom Lieferanten an einen Endkunden über die Lieferung von Energie.
    NETZNUTZUNGSRECHNUNG  #: Eine Rechnung vom Netzbetreiber an den Netznutzer. (i.d.R. der Lieferant) über die Netznutzung.
    MEHRMINDERMENGENRECHNUNG  #: Eine Rechnung vom Netzbetreiber an den Netznutzer. (i.d.R. der Lieferant) zur Abrechnung von Mengen-Differenzen zwischen Bilanzierung und Messung.
    MESSSTELLENBETRIEBSRECHNUNG  #: Rechnung eines Messstellenbetreibers an den Messkunden.
    BESCHAFFUNGSRECHNUNG  #: Rechnungen zwischen einem  Händler und Einkäufer von Energie.
    AUSGLEICHSENERGIERECHNUNG  #: Rechnung an den Verursacher von Ausgleichsenergie.
