"""
Contains RegionalePreisstaffel class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .preisstaffel import Preisstaffel

if TYPE_CHECKING:
    from .regionalegueltigkeit import RegionaleGueltigkeit

# pylint: disable=too-few-public-methods


@postprocess_docstring
class RegionalePreisstaffel(Preisstaffel):
    """
    Mit dieser Komponente können Staffelpreise abgebildet werden, die sich auf eine Region beziehen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RegionalePreisstaffel.json>`_

    """

    typ: Annotated[Literal[ComTyp.REGIONALEPREISSTAFFEL], Field(alias="_typ")] = (
        ComTyp.REGIONALEPREISSTAFFEL  # type:ignore[assignment]
    )

    regionale_gueltigkeit: Optional["RegionaleGueltigkeit"] = None
    """Regionale Eingrenzung der Preisstaffel"""
