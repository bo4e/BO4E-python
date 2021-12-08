# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Gueltigkeitstyp(StrEnum):
    """
    Übersicht der verschiedenen Gültigkeiten zur Umsetzung von Positiv- bzw. Negativlisten.
    """

    NUR_IN = "NUR_IN"  #: Ein so eingeschränktes Merkmal gilt nur mit den angebenen Werten
    NICHT_IN = "NICHT_IN"  #: Ein so eingeschränktes Merkmal gilt nicht mit den angebenen Werten
    NUR_IN_KOMBINATION_MIT = (
        "NUR_IN_KOMBINATION_MIT"  #: Die Kriterien mit diesem Gültigkeitstyp werden miteinander kombiniert
    )
