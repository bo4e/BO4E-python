# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Geraetemerkmal(StrEnum):
    """
    Auflistung möglicher abzurechnender Gerätetypen.
    """

    EINTARIF = "EINTARIF"  #: Eintarifzähler
    ZWEITARIF = "ZWEITARIF"  #: Zweitarifzähler
    MEHRTARIF = "MEHRTARIF"  #: Mehrtarifzähler
    GAS_G2_5 = "GAS_G2_5"  #: Gaszähler Größe G2.5
    GAS_G4 = "GAS_G4"  #: Gaszähler Größe G4
    GAS_G6 = "GAS_G6"  #: Gaszähler Größe G6
    GAS_G10 = "GAS_G10"  #: Gaszähler Größe G10
    GAS_G16 = "GAS_G16"  #: Gaszähler Größe G16
    GAS_G25 = "GAS_G25"  #: Gaszähler Größe G25
    GAS_G40 = "GAS_G40"  #: Gaszähler Größe G40
    GAS_G65 = "GAS_G65"  #: Gaszähler Größe G65
    GAS_G100 = "GAS_G100"  #: Gaszähler Größe G100
    GAS_G160 = "GAS_G160"  #: Gaszähler Größe G160
    GAS_G250 = "GAS_G250"  #: Gaszähler Größe G250
    GAS_G400 = "GAS_G400"  #: Gaszähler Größe G400
    GAS_G650 = "GAS_G650"  #: Gaszähler Größe G650
    GAS_G1000 = "GAS_G1000"  #: Gaszähler Größe G1000
    GAS_G1600 = "GAS_G1600"  #: Gaszähler Größe G1600
    GAS_G2500 = "GAS_G2500"  #: Gaszähler Größe G2500
    IMPULSGEBER_G4_G100 = "IMPULSGEBER_G4_G100"  #: Impulsgeber für Zähler G4 - G100
    IMPULSGEBER_G100 = "IMPULSGEBER_G100"  #: Impulsgeber für Zähler größer G100
    TELEFONANSCHLUSS = "TELEFONANSCHLUSS"  #: Telefonanschluss
    MODEM_GSM = "MODEM_GSM"  #: Modem-GSM
    MODEM_GPRS = "MODEM_GPRS"  #: Modem-GPRS
    MODEM_FUNK = "MODEM_FUNK"  #: Modem-Funk
    MODEM_GSM_O_LG = "MODEM_GSM_O_LG"  #: vom Messstellenbetreiber beigestelltes GSM-Modem ohne Lastgangmessung
    MODEM_GSM_M_LG = "MODEM_GSM_M_LG"  #: vom Messstellenbetreiber beigestelltes GSM-Modem mit Lastgangmessung
    MODEM_FESTNETZ = "MODEM_FESTNETZ"  #: vom Messstellenbetreiber beigestelltes Festnetz-Modem
    MODEM_GPRS_M_LG = "MODEM_GPRS_M_LG"  #: vom Messstellenbetreiber bereitgestelltes GPRS-Modem Lastgangmessung
    PLC_KOM = "PLC_KOM"  #: PLC-Kom.-Einrichtung (Powerline Communication)
    ETHERNET_KOM = "ETHERNET_KOM"  #: Ethernet-Kom.-Einricht. LAN/WLAN
    DSL_KOM = "DSL_KOM"  #: DSL-Kommunikationseinrichtung
    LTE_KOM = "LTE_KOM"  #: LTE-Kommunikationseinrichtung
    KOMPAKT_MU = "KOMPAKT_MU"  #: Kompaktmengenumwerter
    SYSTEM_MU = "SYSTEM_MU"  #: Systemmengenumwerter
    TEMPERATUR_MU = "TEMPERATUR_MU"  #: Temperaturmengenumwerter
    ZUSTANDS_MU = "ZUSTANDS_MU"  #: Zustandsmengenumwerter
    UNBESTIMMT = "UNBESTIMMT"  #: Unbestimmtes Merkmal
