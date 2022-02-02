# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Gebiettyp(StrEnum):
    """
    List of possible Gebiettypen.
    """

    REGELZONE = "REGELZONE"  #: Regelzone
    MARKTGEBIET = "MARKTGEBIET"  #: Marktgebiet
    BILANZIERUNGSGEBIET = "BILANZIERUNGSGEBIET"  #: Bilanzierungsgebiet
    VERTEILNETZ = "VERTEILNETZ"  #: Verteilnetz
    TRANSPORTNETZ = "TRANSPORTNETZ"  #: Transportnetz
    REGIONALNETZ = "REGIONALNETZ"  #: Regionalnetz
    AREALNETZ = "AREALNETZ"  #: Arealnetz
    GRUNDVERSORGUNGSGEBIET = "GRUNDVERSORGUNGSGEBIET"  #: Grundversorgungsgebiet
    VERSORGUNGSGEBIET = "VERSORGUNGSGEBIET"  #: Versorgungsgebiet
