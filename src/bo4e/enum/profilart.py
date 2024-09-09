# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Profilart(StrEnum):
    """
    Diese Enum repräsentiert die verschiedenen Arten von Profilen, die in der BO4E vorkommen können.
    Profilart (temperaturabhängig / standardlastprofil)
    """

    ART_STANDARDLASTPROFIL = "ART_STANDARDLASTPROFIL"
    #: Standardlastprofil
    ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL = "ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL"
    #: Tagesparameterabhängiges Lastprofil
    ART_LASTPROFIL = "ART_LASTPROFIL"
    #: Lastprofil
    ART_STANDARDEINSPEISEPROFIL = "ART_STANDARDEINSPEISEPROFIL"
    #: Standardeinspeiseprofil
    ART_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL = "ART_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL"
    #: Tagesparameterabhängiges Einspeiseprofil
