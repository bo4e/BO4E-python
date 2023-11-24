# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


# pylint: disable=line-too-long
class Geraetetyp(StrEnum):
    """
    Auflistung möglicher abzurechnender Gerätetypen.
    """

    MULTIPLEXANLAGE = "MULTIPLEXANLAGE"  #: Multiplexeranlage
    PAUSCHALANLAGE = "PAUSCHALANLAGE"  #: Pauschalanlagen
    VERSTAERKERANLAGE = "VERSTAERKERANLAGE"  #: Verstärkeranlage
    SUMMATIONSGERAET = "SUMMATIONSGERAET"  #: Summationsgerät
    IMPULSGEBER = "IMPULSGEBER"  #: Impulsgeber
    MENGENUMWERTER = "MENGENUMWERTER"  #: Mengenumwerter
    STROMWANDLER = "STROMWANDLER"  #: Stromwandler
    SPANNUNGSWANDLER = "SPANNUNGSWANDLER"  #: Spannungs-Wandler
    KOMBIMESSWANDLER = "KOMBIMESSWANDLER"  #: Kombimesswandler
    BLOCKSTROMWANDLER = "BLOCKSTROMWANDLER"  #: Blockstromwandler
    DATENLOGGER = "DATENLOGGER"  #: Datenlogger
    KOMMUNIKATIONSANSCHLUSS = "KOMMUNIKATIONSANSCHLUSS"  #: Kommunikationsanschluss
    MODEM = "MODEM"  #: Modem
    TELEKOMMUNIKATIONSEINRICHTUNG = "TELEKOMMUNIKATIONSEINRICHTUNG"  #: vom Messstellenbetreiber beigestellte Telekommunikationseinrichtung (Telefonanschluss)
    MODERNE_MESSEINRICHTUNG = "MODERNE_MESSEINRICHTUNG"  #: moderne Messeinrichtung
    INTELLIGENTES_MESSYSTEM = "INTELLIGENTES_MESSYSTEM"  #: Intelligentes Messystem
    STEUEREINRICHTUNG = "STEUEREINRICHTUNG"  #: Steuereinrichtung
    TARIFSCHALTGERAET = "TARIFSCHALTGERAET"  #: Tarifschaltgerät
    RUNDSTEUEREMPFAENGER = "RUNDSTEUEREMPFAENGER"  #: Rundsteuerempfänger
    OPTIONALE_ZUS_ZAEHLEINRICHTUNG = "OPTIONALE_ZUS_ZAEHLEINRICHTUNG"  #: optionale zusätzliche Zähleinrichtung
    MESSWANDLERSATZ_IMS_MME = "MESSWANDLERSATZ_IMS_MME"  #: Messwandlersatz Strom iMS und mME, NSP
    KOMBIMESSWANDLER_IMS_MME = "KOMBIMESSWANDLER_IMS_MME"  #: Kombimesswandlersatz (Strom u. Spg) iMS und mME
    TARIFSCHALTGERAET_IMS_MME = "TARIFSCHALTGERAET_IMS_MME"  #: Tarifschaltung iMS und mME
    RUNDSTEUEREMPFAENGER_IMS_MME = "RUNDSTEUEREMPFAENGER_IMS_MME"  #: Rundsteuerempfänger iMS und mME
    TEMPERATUR_KOMPENSATION = "TEMPERATUR_KOMPENSATION"  #: Temperaturkompensation
    HOECHSTBELASTUNGS_ANZEIGER = "HOECHSTBELASTUNGS_ANZEIGER"  #: Höchsbelastungsanzeiger
    SONSTIGES_GERAET = "SONSTIGES_GERAET"  #: Sonstiges Gerät
    EDL_21 = "EDL_21"  #: EDL21
    EDL_40_ZAEHLERAUFSATZ = "EDL_40_ZAEHLERAUFSATZ"  #: EDL 40 Zähleraufsatz für Zähler
    EDL_40 = "EDL_40"  #: EDL 40
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
