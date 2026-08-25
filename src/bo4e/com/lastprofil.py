"""
Contains class Lastprofil
"""

from typing import Annotated, Literal

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

    bezeichnung: str | None = None  #: Bezeichnung des Profils, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    profilschar: str | None = None  #: Bezeichnung der Profilschar, durch DVGW bzw. den Netzbetreiber vergeben (z.B. H0)
    verfahren: Profilverfahren | None = None  #: Verfahren des Profils (analytisch oder synthetisch)
    ist_einspeisung: bool | None = None  #: Einspeiseprofil: True/False
    tagesparameter: Tagesparameter | None = None  #: Klimazone / Temperaturmessstelle
    profilart: Profilart | None = None  #: Profilart des Lastprofils, e.g. ART_STANDARDLASTPROFIL
    herausgeber: str | None = None  #: Herausgeber des Lastprofil-Codes, e.g. BDEW
