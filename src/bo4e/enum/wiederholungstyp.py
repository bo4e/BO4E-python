# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Wiederholungstyp(StrEnum):
    """
    Klassifiziert einen Tagtyp, an dem ein wiederkehrendes Schaltschema (z.B. die Umschaltzeiten einer
    `Zaehlzeitdefinition`) gilt. Die Werte teilen sich in drei Gruppen auf:

    * `TAEGLICH` – gilt an jedem Tag des Jahres.
    * Gruppenbezeichnungen (`WERKTAGS`, `WOCHENENDE`, `FEIERTAGS`) – fassen mehrere Wochentage zusammen.
      Was als Feiertag zählt, wird durch den Feiertagskalender der `Zaehlzeitdefinition` bestimmt.
    * Einzelne Wochentage (`MONTAGS` … `SONNTAGS`).
    """

    TAEGLICH = "TAEGLICH"
    WERKTAGS = "WERKTAGS"
    WOCHENENDE = "WOCHENENDE"
    FEIERTAGS = "FEIERTAGS"

    MONTAGS = "MONTAGS"
    DIENSTAGS = "DIENSTAGS"
    MITTWOCHS = "MITTWOCHS"
    DONNERSTAGS = "DONNERSTAGS"
    FREITAGS = "FREITAGS"
    SAMSTAGS = "SAMSTAGS"
    SONNTAGS = "SONNTAGS"
