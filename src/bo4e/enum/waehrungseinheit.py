# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class Waehrungseinheit(StrEnum):
    """
    In diesem Enum werden die Währungen und ihre Untereinheiten definiert, beispielsweise für die Verwendung in Preisen.
    """

    EUR = "EUR"  #: Euro
    CT = "CT"  #: Eurocent
