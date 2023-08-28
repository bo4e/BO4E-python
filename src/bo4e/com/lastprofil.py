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

    bezeichnung: Optional[str] = None  #: Bezeichnung des Profils, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    profilschar: Optional[
        str
    ] = None  #: Bezeichnung der Profilschar, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    verfahren: Optional[Profilverfahren] = None  #: Verfahren des Profils (analytisch oder synthetisch)
    einspeisung: Optional[bool] = None
    """
        Einspeiseprofil:
        
            True/False
    """
    tagesparameter: Optional[Tagesparameter] = None  #: Klimazone / Temperaturmessstelle
    profilart: Optional[Profilart] = None  #: Profilart des Lastprofils, e.g. ART_STANDARDLASTPROFIL
    herausgeber: Optional[str] = None  #: Herausgeber des Lastprofil-Codes, e.g. BDEW

    _tagesparameter_check = field_validator("profilart")(tagesparameter_given_for_tagesparam_lastprofil)
    """ 
    Field validator for profilart.
    Tagesparameter needs to be set if profilart is depended on daily parameters.
    """
