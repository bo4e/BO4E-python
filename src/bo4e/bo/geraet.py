"""
Contains Geraet class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..enum.geraeteklasse import Geraeteklasse
from ..enum.geraetetyp import Geraetetyp
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Geraet(Geschaeftsobjekt):
    """
    Mit diesem BO werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Geraet.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.GERAET

    #: Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird.
    geraetenummer: Optional[str] = None
    #: Bezeichnung des Geräts
    bezeichnung: Optional[str] = None
    #: Die übergreifende Klasse eines Geräts, beispielsweise Wandler
    geraeteklasse: Optional[Geraeteklasse] = None
    #: Der speziellere Typ eines Gerätes, beispielsweise Stromwandler
    geraetetyp: Optional[Geraetetyp] = None
