# pylint: disable=missing-module-docstring,line-too-long
from bo4e.enum.strenum import StrEnum


class Rechnungsstatus(StrEnum):
    """
    Abbildung verschiedener Zustände, die im Rahmen der Rechnungsbearbeitung durchlaufen werden.
    """

    UNGEPRUEFT = "UNGEPRUEFT"  #: Die Rechnung wurde erstellt bzw ist eingegangen, wurde aber noch nicht geprüft.
    GEPRUEFT_OK = "GEPRUEFT_OK"  #: Die Rechnung wurde geprüft und als korrekt befunden.
    GEPRUEFT_FEHLERHAFT = "GEPRUEFT_FEHLERHAFT"  #: Bei der Prüfung der Rechnung hat sich herausgestellt, dass die Rechnung Fehler aufweist.
    GEBUCHT = "GEBUCHT"  #: Die Buchhaltung hat die Rechnung aufgenommen und berücksichtigt.
    BEZAHLT = "BEZAHLT"  #: Die Rechnung wurde beglichen.
