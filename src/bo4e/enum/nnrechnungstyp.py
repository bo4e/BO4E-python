# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class NNRechnungstyp(StrEnum):
    """
    Abbildung verschiedener in der INVOIC angegebenen Rechnungstypen.
    """

    ABSCHLUSSRECHNUNG  #: Abschlussrechnung
    ABSCHLAGSRECHNUNG  #: Abschlagsrechnung
    TURNUSRECHNUNG  #: Turnusrechnung
    MONATSRECHNUNG  #: Monatsrechnung
    WIMRECHNUNG  #: Rechnung für WiM
    ZWISCHENRECHNUNG  #: Zwischenrechnung
    INTEGRIERTE_13TE_RECHNUNG  #: Integrierte 13. Rechnung
    ZUSAETZLICHE_13TE_RECHNUNG  #: 13. Rechnung
    MEHRMINDERMENGENRECHNUNG  #: Mehr/Mindermengenabrechnung
