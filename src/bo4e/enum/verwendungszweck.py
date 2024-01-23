# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Verwendungszweck(StrEnum):
    """
    Verwendungszweck der Werte Marktlokation
    """

    NETZNUTZUNGSABRECHNUNG = "NETZNUTZUNGSABRECHNUNG"  #: Netznutzungsabrechnung
    BILANZKREISABRECHNUNG = "BILANZKREISABRECHNUNG"  #: Bilanzkreisabrechnung
    MEHRMINDERMENGENABRECHNUNG = "MEHRMINDERMENGENABRECHNUNG"  #: Mehrmindermengenabrechnung
    ENDKUNDENABRECHNUNG = "ENDKUNDENABRECHNUNG"  #: Endkundenabrechnung
    UEBERMITTLUNG_AN_DAS_HKNR = "UEBERMITTLUNG_AN_DAS_HKNR"  #: Übermittlung an das Herkunftsnachweisregister (HKNR)
    #: Zur Ermittlung der Ausgeglichenheit von Bilanzkreisen
    ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS = "ERMITTLUNG_AUSGEGLICHENHEIT_BILANZKREIS"
