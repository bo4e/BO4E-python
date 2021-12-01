# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Regionskriteriumtyp(StrEnum):
    """
    Klassifizierung der Kriterien für eine regionale Eingrenzung.
    """

    BUNDESLANDKENNZIFFER = "BUNDESLANDKENNZIFFER"  #: offizielle Bundeslandkennziffer
    BUNDESLAND_NAME = "BUNDESLAND_NAME"  #: Bundesland Name
    MARKTGEBIET_NUMMER = "MARKTGEBIET_NUMMER"  #: offizielle Marktgebiet-Codenummer
    MARKTGEBIET_NAME = "MARKTGEBIET_NAME"  #: Marktgebiet Name
    REGELGEBIET_NUMMER = "REGELGEBIET_NUMMER"  #: offizielle Regelgebiet Nummer
    REGELGEBIET_NAME = "REGELGEBIET_NAME"  #: Regelgebiet Name
    NETZ_STROM = "NETZ_STROM"  #: Identifikation des Netzes Strom
    NETZ_GAS = "NETZ_GAS"  #: Identifikation des Netzes Gas
    NETZBETREIBER_NUMMER_STROM = "NETZBETREIBER_NUMMER_STROM"  #: offizielle Netzbetreiber-Codenummer Strom
    NETZBETREIBER_NUMMER_GAS = "NETZBETREIBER_NUMMER_GAS"  #: offizielle Netzbetreiber-Codenummer Gas
    NETZBETREIBER_NAME_STROM = "NETZBETREIBER_NAME_STROM"  #: Netzbetreiber Name Strom
    NETZBETREIBER_NAME_GAS = "NETZBETREIBER_NAME_GAS"  #: Netzbetreiber Name Gas
    BILANZIERUNGS_GEBIET_NUMMER = (
        "BILANZIERUNGS_GEBIET_NUMMER"  #: Strom: Bilanzierungsgebietsnummer, Gas: Netzkontonummer
    )
    MSB_NUMMER = "MSB_NUMMER"  #: offizielle Messstellenbetreiber-Codenummer
    MSB_NAME = "MSB_NAME"  #: Name des MSB
    VERSORGER_NUMMER = "VERSORGER_NUMMER"  #: offizielle Lieferanten-Codenummer eines Versorgers
    VERSORGER_NAME = "VERSORGER_NAME"  #: Name eines Versorgers
    GRUNDVERSORGER_NUMMER_STROM = (
        "GRUNDVERSORGER_NUMMER_STROM"  #: offizielle Lieferanten-Codenummer des Strom-Grundversorgers
    )
    GRUNDVERSORGER_NAME_STROM = "GRUNDVERSORGER_NAME_STROM"  #: Name des Strom-Grundversorgers
    GRUNDVERSORGER_NUMMER_GAS = (
        "GRUNDVERSORGER_NUMMER_GAS"  #: offizielle Lieferanten-Codenummer des Gas-Grundversorgers
    )
    GRUNDVERSORGER_NAME_GAS = "GRUNDVERSORGER_NAME_GAS"  #: Name des Gas-Grundversorgers
    KREIS_NAME = "KREIS_NAME"  #: Kreis
    KREISKENNZIFFER = "KREISKENNZIFFER"  #: offizielle Kreiskennziffer
    GEMEINDE_NAME = "GEMEINDE_NAME"  #: Gemeinde
    GEMEINDEKENNZIFFER = "GEMEINDEKENNZIFFER"  #: offizielle Gemeindekennziffer
    POSTLEITZAHL = "POSTLEITZAHL"  #: Postleitzahl
    ORT = "ORT"  #: Ort
    POSTORT = "POSTORT"  #: Kriterium bestehend aus Postleitzahl und Ort
    EINWOHNERZAHL_GEMEINDE = "EINWOHNERZAHL_GEMEINDE"  #: Einwohnerzahl Gemeinde
    EINWOHNERZAHL_ORT = "EINWOHNERZAHL_ORT"  #: Einwohnerzahl Ort
    KM_UMKREIS = "KM_UMKREIS"  #: km Umkreis
    BUNDESWEIT = "BUNDESWEIT"  #: Bundesweite Betrachtung
    PLZ_BEREICH = "PLZ_BEREICH"  #: Postleitzahlenbereich
