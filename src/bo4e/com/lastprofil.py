"""
Contains class Lastprofil
"""
from typing import Optional

from pydantic import field_validator

from bo4e.com.com import COM
from bo4e.com.tagesparameter import Tagesparameter
from bo4e.enum.profilart import Profilart
from bo4e.enum.profilverfahren import Profilverfahren
from bo4e.validators import tagesparameter_given_for_tagesparam_lastprofil


class Lastprofil(COM):
    """
    Lastprofil
    """

    #: Bezeichnung des Profils, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    bezeichnung: Optional[str] = None
    #: Optionale Bezeichnung der Profilschar, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    profilschar: Optional[str] = None
    #: Verfahren des Profils (analytisch oder synthetisch)
    verfahren: Optional[Profilverfahren] = None
    #: Einspeiseprofil: True/False
    einspeisung: Optional[bool] = None
    #: Klimazone / Temperaturmessstelle
    tagesparameter: Optional[Tagesparameter] = None
    #: Profilart des Lastprofils, e.g. ART_STANDARDLASTPROFIL
    profilart: Optional[Profilart] = None
    """ 
    Field validator für Profilart.
    Wenn die Profilart tagesparameterabh. ist, muss ein Tagesparameter gegeben sein.
    """
    _tagesparameter_check = field_validator("profilart")(tagesparameter_given_for_tagesparam_lastprofil)
    #: Herausgeber des Lastprofil-Codes, e.g. BDEW
    herausgeber: Optional[str] = None
