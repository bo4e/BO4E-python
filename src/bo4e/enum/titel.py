# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Titel(StrEnum):
    """
    Übersicht möglicher Titel, z.B. eines Geschäftspartners.
    """

    DR = "DR"  #: Doktor*In
    PROF = "PROF"  #: Professor*In
    PROF_DR = "PROF_DR"  #: Professor*In Dr.
