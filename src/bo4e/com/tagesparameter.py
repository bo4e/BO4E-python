"""
contains tagesparameter class
"""


from typing import Optional

from bo4e.com.com import COM


class Tagesparameter(COM):
    """
    Speichert Informationen zu einer tagesparameter abhängigen Messstelle. z.B. den Namen einer Klimazone oder die ID
    der Wetterstation für die Temperaturmessstelle
    """
    # optional attributes
    #: Qualifier der Klimazone, e.g. 7624q
    klimazone: Optional[str] = None
    #: Qualifier der Temperaturmessstelle, e.g. 1234x
    temperaturmessstelle: Optional[str] = None
    #: Dienstanbieter (bei Temperaturmessstellen), e.g. ZT1
    dienstanbieter: Optional[str] = None
    #: Herausgeber des Lastprofil-Codes, e.g. BDEW
    herausgeber: Optional[str] = None
