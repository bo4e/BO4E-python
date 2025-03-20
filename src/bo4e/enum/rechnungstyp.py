# pylint: disable=missing-module-docstring, line-too-long
from bo4e.enum.strenum import StrEnum


class Rechnungstyp(StrEnum):
    """
    Abbildung verschiedener Rechnungstypen zur Kennzeichnung von Rechnungen
    """

    ENDKUNDENRECHNUNG = "ENDKUNDENRECHNUNG"
    """Eine Rechnung vom Lieferanten an einen Endkunden über die Lieferung von Energie."""
    NETZNUTZUNGSRECHNUNG = "NETZNUTZUNGSRECHNUNG"
    """Eine Rechnung vom Netzbetreiber an den Netznutzer. (i.d.R. der Lieferant) über die Netznutzung."""
    MEHRMINDERMENGENRECHNUNG = "MEHRMINDERMENGENRECHNUNG"
    """Eine Rechnung vom Netzbetreiber an den Netznutzer. (i.d.R. der Lieferant) zur Abrechnung von Mengen-Differenzen zwischen Bilanzierung und Messung."""
    MESSSTELLENBETRIEBSRECHNUNG = "MESSSTELLENBETRIEBSRECHNUNG"
    """Rechnung eines Messstellenbetreibers an den Messkunden."""
    BESCHAFFUNGSRECHNUNG = "BESCHAFFUNGSRECHNUNG"
    """Rechnungen zwischen einem  Händler und Einkäufer von Energie."""
    AUSGLEICHSENERGIERECHNUNG = "AUSGLEICHSENERGIERECHNUNG"
    """Rechnung an den Verursacher von Ausgleichsenergie."""
    ABSCHLUSSRECHNUNG = "ABSCHLUSSRECHNUNG"  #: ABSCHLUSSRECHNUNG
    ABSCHLAGSRECHNUNG = "ABSCHLAGSRECHNUNG"  #: ABSCHLAGSRECHNUNG
    TURNUSRECHNUNG = "TURNUSRECHNUNG"  #: TURNUSRECHNUNG
    MONATSRECHNUNG = "MONATSRECHNUNG"  #: MONATSRECHNUNG
    ZWISCHENRECHNUNG = "ZWISCHENRECHNUNG"  #: ZWISCHENRECHNUNG
    INTEGRIERTE_13TE_RECHNUNG = "INTEGRIERTE_13TE_RECHNUNG"  #: INTEGRIERTE_13TE_RECHNUNG
    ZUSAETZLICHE_13TE_RECHNUNG = "ZUSAETZLICHE_13TE_RECHNUNG"  #: ZUSAETZLICHE_13TE_RECHNUNG
