# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class EEGVermarktungsform(StrEnum):
    """
    Diese Enum repräsentiert die Vermarktungsformen nach dem EEG.
    """

    AUSFALLVERGUETUNG = "AUSFALLVERGUETUNG"  #: Ausfallvergütung
    # Ausfallvergütung für den Fall, dass andere Vermarktungsmethoden nicht verfügbar sind
    MARKTPRAEMIE = "MARKTPRAEMIE"  #: Marktprämie
    # Marktprämie für die geförderte Direktvermarktung
    SONSTIGES = "SONSTIGES"  #: Sonstiges
    # Sonstige Vermarktungsformen ohne gesetzliche Vergütung
    KWKG_VERGUETUNG = "KWKG_VERGUETUNG"  #: KWKG-Vergütung
    # Vergütung nach dem Kraft-Wärme-Kopplungsgesetz (KWKG)
