"""
Contains LastvariablePreisposition class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.preisreferenz import Preisreferenz
    from ..enum.tarifkalkulationsmethode import Tarifkalkulationsmethode
    from ..enum.waehrungseinheit import Waehrungseinheit
    from .preisstaffel import Preisstaffel


@postprocess_docstring
class LastvariablePreisposition(COM):
    """
    Modelliert eine lastvariable Preisposition.

    .. raw:: html

        <object data="../_static/images/bo4e/com/LastvariablePreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `LastvariablePreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/LastvariablePreisposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.LASTVARIABLEPREISPOSITION], Field(alias="_typ")] = ComTyp.LASTVARIABLEPREISPOSITION

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für die Preisposition."""
    preisreferenz: Optional["Preisreferenz"] = None
    """
    Die Referenz worauf sich der Preis bezieht.
    Die explizite Einheit wird durch das Feld `preis_bezugseinheit` angegeben.
    """
    preis_waehrungseinheit: Optional["Waehrungseinheit"] = None
    """Währungseinheit für die Preise in allen Preisstaffeln, z.B. Euro oder Ct."""
    preis_bezugseinheit: Optional["Mengeneinheit"] = None
    """Angabe, für welche Bezugsgröße die Preise in den Preisstaffeln gelten. Z.B. kWh."""
    staffelgrenzeneinheit: Optional["Mengeneinheit"] = None
    """Die Einheit, in denen die Staffelgrenzen in den Preisstaffeln angegeben sind."""
    tarifkalkulationsmethode: Optional["Tarifkalkulationsmethode"] = None
    """Das Modell, das der Preisbildung zugrunde liegt"""
    preisstaffeln: Optional[list["Preisstaffel"]] = None
    """Preisstaffeln, die zu dieser Preisposition gehören"""
