# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Geschaeftspartnerrolle(StrEnum):
    """
    Diese Rollen kann ein Geschäftspartner einnehmen.

    Profilart (temperaturabhängig / standardlastprofil)
    """

    ART_STANDARDLASTPROFILOBJ = "ART_STANDARDLASTPROFILOBJ"
    #: Standardlastprofil
    ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL = "ART_TAGESPARAMETERABHAENGIGES_LASTPROFIL"
    #: Tagesparameterabhängiges Lastprofil
    ART_LASTPROFIL = "ART_LASTPROFIL"
    #: Lastprofil
    ART_STANDARDEINSPEISEPROFIL = "ART_STANDARDEINSPEISEPROFIL"
    #: Standardeinspeiseprofil
    ART_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL = "ART_TAGESPARAMETERABHAENGIGES_EINSPEISEPROFIL"
    #: Tagesparameterabhängiges Einspeiseprofil
