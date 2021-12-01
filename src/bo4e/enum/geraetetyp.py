# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


# pylint: disable=line-too-long
class Geraetetyp(StrEnum):
    """
    Auflistung möglicher abzurechnender Gerätetypen.
    """

    WECHSELSTROMZAEHLER = "WECHSELSTROMZAEHLER"  #: Wechselstromzähler
    DREHSTROMZAEHLER = "DREHSTROMZAEHLER"  #: Drehstromzähler
    ZWEIRICHTUNGSZAEHLER = "ZWEIRICHTUNGSZAEHLER"  #: Zweirichtungszähler
    RLM_ZAEHLER = "RLM_ZAEHLER"  #: RLM-Zähler
    BALGENGASZAEHLER = "BALGENGASZAEHLER"  #: Balgengaszähler
    MAXIMUMZAEHLER = "MAXIMUMZAEHLER"  #: Maximumzähler (Schleppzähler)
    MULTIPLEXANLAGE = "MULTIPLEXANLAGE"  #: Multiplexeranlage
    PAUSCHALANLAGE = "PAUSCHALANLAGE"  #: Pauschalanlagen
    VERSTAERKERANLAGE = "VERSTAERKERANLAGE"  #: Verstärkeranlage
    SUMMATIONSGERAET = "SUMMATIONSGERAET"  #: Summationsgerät
    IMPULSGEBER = "IMPULSGEBER"  #: Impulsgeber
    EDL_21_ZAEHLERAUFSATZ = "EDL_21_ZAEHLERAUFSATZ"  #: EDL 21 Zähleraufsatz für Zähler
    VIER_QUADRANTEN_LASTGANGZAEHLER = "VIER_QUADRANTEN_LASTGANGZAEHLER"  #: Vier-Quadranten-Lastgangzähler
    MENGENUMWERTER = "MENGENUMWERTER"  #: Mengenumwerter
    STROMWANDLER = "STROMWANDLER"  #: Stromwandler
    SPANNUNGSWANDLER = "SPANNUNGSWANDLER"  #: Spannungs-Wandler
    KOMBIMESSWANDLER = "KOMBIMESSWANDLER"  #: Kombimesswandler
    BLOCKSTROMWANDLER = "BLOCKSTROMWANDLER"  #: Blockstromwandler
    DATENLOGGER = "DATENLOGGER"  #: Datenlogger
    KOMMUNIKATIONSANSCHLUSS = "KOMMUNIKATIONSANSCHLUSS"  #: Kommunikationsanschluss
    MODEM = "MODEM"  #: Modem
    TELEKOMMUNIKATIONSEINRICHTUNG = "TELEKOMMUNIKATIONSEINRICHTUNG"  #: vom Messstellenbetreiber beigestellte Telekommunikationseinrichtung (Telefonanschluss)
    DREHKOLBENGASZAEHLER = "DREHKOLBENGASZAEHLER"  #: Drehkolbengaszähler
    TURBINENRADGASZAEHLER = "TURBINENRADGASZAEHLER"  #: Turbinenradgaszähler
    ULTRASCHALLZAEHLER = "ULTRASCHALLZAEHLER"  #: Ultraschallzähler
    WIRBELGASZAEHLER = "WIRBELGASZAEHLER"  #: Wirbelgaszähler
    MODERNE_MESSEINRICHTUNG = "MODERNE_MESSEINRICHTUNG"  #: moderne Messeinrichtung
    INTELLIGENTES_MESSYSTEM = "INTELLIGENTES_MESSYSTEM"  #: Intelligentes Messystem
    ELEKTRONISCHER_HAUSHALTSZAEHLER = "ELEKTRONISCHER_HAUSHALTSZAEHLER"  #: elektronischer Haushaltszähler
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
    PREPAYMENTZAEHLER = "PREPAYMENTZAEHLER"  #: Prepaymentzähler
    EDL_21 = "EDL_21"  #: EDL21
    _96_H_ZAEHLER = "96_H_ZAEHLER"  #: 96 h Zähler
    EDL_40_ZAEHLERAUFSATZ = "EDL_40_ZAEHLERAUFSATZ"  #: EDL 40 Zähleraufsatz für Zähler
