# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class AufAbschlagstyp(StrEnum):
    """
    Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten Werten erfolgt.
    """

    RELATIV = "RELATIV"  #: prozentualer Auf-/Abschlag
    ABSOLUT = "ABSOLUT"  #: Absoluter Auf-/Abschlag
