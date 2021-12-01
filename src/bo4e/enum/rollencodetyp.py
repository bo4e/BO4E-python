# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class Rollencodetyp(StrEnum):
    """
    Gibt den Codetyp einer Rolle, beispielsweise einer Marktrolle, an.
    """

    BDEW = "BDEW"  #: Bundesverband der Energie- u. Wasserwirtschaft
    DVG = "DVG"  #: Deutscher Verein des Gas- und Wasserfaches
    GLN = "GLN"  #: Global Location Number
