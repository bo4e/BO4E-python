"""
Contains Netzlokation class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Annotated, Optional

from pydantic import Field

from ..com.konfigurationsprodukt import Konfigurationsprodukt
from ..com.menge import Menge
from ..com.verwendungszweckpromarktrolle import VerwendungszweckProMarktrolle
from ..enum.marktrolle import Marktrolle
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Netzlokation(Geschaeftsobjekt):
    """
    Object containing information about a Netzlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Netzlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Netzlokation.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.NETZLOKATION

    netzlokations_id: Optional[str] = None
    sparte: Optional[Sparte] = None
    netzanschlussleistung: Optional[Menge] = None
    grundzustaendiger_msb_codenr: Optional[str] = None
    steuerkanal: Optional[bool] = None
    obiskennzahl: Optional[str] = None
    verwendungszweck: Optional[VerwendungszweckProMarktrolle] = None
    konfigurationsprodukte: Optional[list[Konfigurationsprodukt]] = None
    eigenschaft_msb_lokation: Optional[Marktrolle] = None
