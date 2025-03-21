"""
Contains RegionalePreisgarantie class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .preisgarantie import Preisgarantie

if TYPE_CHECKING:
    from .regionalegueltigkeit import RegionaleGueltigkeit

# pylint: disable=too-few-public-methods


@postprocess_docstring
class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RegionalePreisgarantie.json>`_

    """

    typ: Annotated[Literal[ComTyp.REGIONALEPREISGARANTIE], Field(alias="_typ")] = (
        ComTyp.REGIONALEPREISGARANTIE  # type:ignore[assignment]
    )

    regionale_gueltigkeit: Optional["RegionaleGueltigkeit"] = None
    """Regionale Eingrenzung der Preisgarantie."""
