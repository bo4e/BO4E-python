"""
Contains class Lastprofil
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from bo4e.com.com import COM
from bo4e.com.tagesparameter import Tagesparameter
from bo4e.enum.comtyp import ComTyp
from bo4e.enum.profilart import Profilart
from bo4e.enum.profilverfahren import Profilverfahren


class Lastprofil(COM):
    """
    Informationen zum Lastprofil.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Lastprofil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lastprofil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Lastprofil.json>`_

    """

    typ: Annotated[Literal[ComTyp.LASTPROFIL], Field(alias="_typ")] = ComTyp.LASTPROFIL

    bezeichnung: Optional[str] = None  #: Bezeichnung des Profils, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    profilschar: Optional[str] = (
        None  #: Bezeichnung der Profilschar, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    )
    verfahren: Optional[Profilverfahren] = None  #: Verfahren des Profils (analytisch oder synthetisch)
    ist_einspeisung: Optional[bool] = None  #: Einspeiseprofil: True/False
    tagesparameter: Optional[Tagesparameter] = None  #: Klimazone / Temperaturmessstelle
    profilart: Optional[Profilart] = None  #: Profilart des Lastprofils, e.g. ART_STANDARDLASTPROFIL
    herausgeber: Optional[str] = None  #: Herausgeber des Lastprofil-Codes, e.g. BDEW
