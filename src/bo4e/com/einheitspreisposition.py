"""
Contains EinheitsPreisposition class
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
    from .preis import Preis


@postprocess_docstring
class EinheitsPreisposition(COM):
    """
    Die Einheits-Preisposition modelliert Preispositionen ohne Variabilität
    (bis auf die übergeordnete Variabilität durch eine Zeitscheibe und einer Region).

    Dies kann z.B. ein Arbeitspreis sein. Der Bezug wird dabei durch die Preisreferenz angegeben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/EinheitsPreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `EinheitsPreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/EinheitsPreisposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.EINHEITSPREISPOSITION], Field(alias="_typ")] = ComTyp.EINHEITSPREISPOSITION

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für die Preisposition."""
    preisreferenz: Optional["Preisreferenz"] = None
    """
    Die Referenz worauf sich der Preis bezieht.
    Die explizite Einheit wird durch das Feld `bezugswert` im `COM Preis` angegeben.
    """
    preis: Optional["Preis"] = None
    """Der Preis für diese Position."""
