"""
Contains Regionskriterium class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.operator import Operator
    from ..enum.regionskriterium import Regionskriterium


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Regionsoperation(COM):
    """
    Komponente zur Abbildung einer Regionsoperation.

    In Kombination mit anderen Regionsoperationen kann eine Region definiert werden. Eine Regionsoperation ermöglicht
    die Definition einer Region in eingeschränkter Form. Durch den Operator können mehrere "einfache" Regionsoperationen
    miteinander kombiniert werden, um eine komplexere Region zu definieren.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Regionsoperation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionsoperation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Regionsoperation.json>`_

    """

    typ: Annotated[Literal[ComTyp.REGIONSOPERATION], Field(alias="_typ")] = ComTyp.REGIONSOPERATION

    regionsoperator: Optional["Operator"] = None
    prioritaet: int | None = None
    """
    Priorität dieser Regionsoperation. Theoretisch sind Listen in JSON sortiert, jedoch ist eine solche Sortierung
    eventuell implementierungsbedingt fehleranfällig. Daher nutzen wir dieses Feld. angefangen bei 1 (höchste Priorität) und aufsteigend
    """
    bezeichnung: str | None = None
    """(auch IDs und PLZ möglich)"""
    bezeichnung2: str | None = None
    """(TODO: bessere Benamung! geht vor allem um Postort: PLZ & Ort als Schnittmenge)"""
    wert_von: str | None = None
    """(inklusiv)"""
    wert_bis: str | None = None
    """(inklusiv)"""
    radius_in_km: Decimal | None = None
    """(inklusiv)"""
    regionskriterium: Optional["Regionskriterium"] = None
    """(ehemals Regionskriteriumtyp)]"""
