"""
Contains DynamischePreisposition class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.preisreferenz import Preisreferenz


@postprocess_docstring
class DynamischePreisposition(COM):
    """
    Modelliert eine dynamische Preisposition.

    Diese Preisposition enthält lediglich eine Referenz zum Börsenindex, auf den sie sich bezieht. Das Format dieser
    Referenz ist vom Standard nicht spezifiziert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/DynamischePreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `DynamischePreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/DynamischePreisposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.DYNAMISCHEPREISPOSITION], Field(alias="_typ")] = ComTyp.DYNAMISCHEPREISPOSITION

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für die Preisposition."""
    preisreferenz: Optional["Preisreferenz"] = None
    """
    Die Referenz worauf sich der Preis bezieht.
    Die explizite Einheit wird durch das Feld `preis_bezugseinheit` angegeben.
    """
    index: Optional[str] = None
    """
    Eine Referenz zum Börsenindex dieser dynamischen Preisposition.
    Das genaue Format ist vom Standard nicht spezifiziert.
    """
