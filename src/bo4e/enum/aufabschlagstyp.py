# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class AufAbschlagstyp(StrEnum):
    """
    Festlegung, ob der Auf- oder Abschlag mit relativen oder absoluten Werten erfolgt.
    """

    RELATIV  #: prozentualer AufAbschlag
    ABSOLUT  #: Absoluter AufAbschlag
