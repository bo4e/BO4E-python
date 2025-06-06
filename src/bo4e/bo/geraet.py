"""
Contains Geraet class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..enum.geraeteklasse import Geraeteklasse
    from ..enum.geraetetyp import Geraetetyp


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Geraet(Geschaeftsobjekt):
    """
    Mit diesem BO werden alle Geräte modelliert, die keine Zähler sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Geraet.svg" type="image/svg+xml"></object>

    .. HINT::
        `Geraet JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Geraet.json>`_

    """

    typ: Annotated[Literal[BoTyp.GERAET], Field(alias="_typ")] = BoTyp.GERAET

    geraetenummer: Optional[str] = None
    """Die auf dem Gerät aufgedruckte Nummer, die vom MSB vergeben wird."""
    bezeichnung: Optional[str] = None
    """Bezeichnung des Geräts"""
    geraeteklasse: Optional["Geraeteklasse"] = None
    """Die übergreifende Klasse eines Geräts, beispielsweise Wandler"""
    geraetetyp: Optional["Geraetetyp"] = None
    """Der speziellere Typ eines Gerätes, beispielsweise Stromwandler"""
