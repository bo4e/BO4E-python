# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Rechnungsstatus(StrEnum):
    """
    Abbildung verschiedener Zustände, die im Rahmen der Rechnungsbearbeitung durchlaufen werden.
    """

    UNGEPRUEFT  #: Die Rechnung wurde erstellt bzw ist eingegangen, wurde aber noch nicht geprüft.
    GEPRUEFT_OK  #: Die Rechnung wurde geprüft und als korrekt befunden.
    GEPRUEFT_FEHLERHAFT  #: Bei der Prüfung der Rechnung hat sich herausgestellt, dass die Rechnung Fehler aufweist.
    GEBUCHT  #: Die Buchhaltung hat die Rechnung aufgenommen und berücksichtigt.
    BEZAHLT  #: Die Rechnung wurde beglichen.
