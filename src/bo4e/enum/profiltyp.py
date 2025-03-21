"""
Contains Enums for Profiltyp.
"""

from bo4e.enum.strenum import StrEnum


class Profiltyp(StrEnum):
    """
    Profiltyp (temperaturabhängig / Standardlastprofil).
    """

    SLP_SEP = "SLP_SEP"  #: SLP/SEP
    TLP_TEP = "TLP_TEP"  #: TLP/TEP
