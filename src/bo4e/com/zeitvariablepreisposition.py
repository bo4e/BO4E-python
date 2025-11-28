"""
Contains ZeitvariablePreisposition class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..bo.zaehlzeitdefinition import Zaehlzeitdefinition
    from ..enum.preisreferenz import Preisreferenz
    from .preis import Preis


@postprocess_docstring
class ZeitvariablePreisposition(COM):
    """
    Modelliert eine zeitvariable Preisposition.

    .. raw:: html

        <object data="../_static/images/bo4e/com/ZeitvariablePreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `ZeitvariablePreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/ZeitvariablePreisposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZEITVARIABLEPREISPOSITION], Field(alias="_typ")] = ComTyp.ZEITVARIABLEPREISPOSITION

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für die Preisposition."""
    preisreferenz: Optional["Preisreferenz"] = None
    """
    Die Referenz worauf sich der Preis bezieht.
    Die explizite Einheit wird durch das Feld `bezugswert` im `COM Preis` angegeben.
    """
    preis: Optional["Preis"] = None
    """Der Preis für diese Position."""
    zaehlzeitdefinition: Optional["Zaehlzeitdefinition"] = None
