"""
Contains tagesparameter class
"""

from typing import Annotated, Literal

from pydantic import Field

from bo4e.com.com import COM

from ..enum.comtyp import ComTyp


class Tagesparameter(COM):
    """
    Speichert Informationen zu einer tagesparameter abhängigen Messstelle. z.B. den Namen einer Klimazone oder die ID
    der Wetterstation für die Temperaturmessstelle
    """

    typ: Annotated[Literal[ComTyp.TAGESPARAMETER], Field(alias="_typ")] = ComTyp.TAGESPARAMETER

    klimazone: str | None = None  #: Qualifier der Klimazone, e.g. 7624q
    temperaturmessstelle: str | None = None  #: Qualifier der Temperaturmessstelle, e.g. 1234x
    dienstanbieter: str | None = None  #: Dienstanbieter (bei Temperaturmessstellen), e.g. ZT1
    herausgeber: str | None = None  #: Herausgeber des Lastprofil-Codes, e.g. BDEW
