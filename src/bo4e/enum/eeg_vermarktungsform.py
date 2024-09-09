# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class EEGVermarktungsform(StrEnum):
    """
    Diese Enum repräsentiert die Vermarktungsformen nach dem EEG.
    """

    AUSFALLVERGUETUNG = "AUSFALLVERGUETUNG"
    # Ausfallvergütung für den Fall, dass andere Vermarktungsmethoden nicht verfügbar sind

    MARKTPRAEMIE = "MARKTPRAEMIE"
    # Marktprämie für die geförderte Direktvermarktung

    SONSTIGE = "SONSTIGE"
    # Sonstige Vermarktungsformen ohne gesetzliche Vergütung

    KWKG_VERGUETUNG = "KWKG_VERGUETUNG"
    # Vergütung nach dem Kraft-Wärme-Kopplungsgesetz (KWKG)
