"""
Contains Zaehlzeitsaison class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from .zaehlzeittagtyp import Zaehlzeittagtyp


@postprocess_docstring
class Zaehlzeitsaison(COM):
    """
    Bündelt alle Schaltschemata, die innerhalb einer Saison einer `Zaehlzeitdefinition` gelten.

    Eine Saison ist ein Teil des Jahres, in dem dieselben Schaltschemata gelten – typischerweise
    Sommer und Winter. Welche Tage zu welcher Saison gehören, wird nicht in diesem COM, sondern
    über das `saisonprofil` der übergeordneten `Zaehlzeitdefinition` festgelegt; `bezeichnung`
    bildet hier die textuelle Verknüpfung zwischen Profil und Saisonabschnitt.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zaehlzeitsaison.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitsaison JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zaehlzeitsaison.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZAEHLZEITSAISON], Field(alias="_typ")] = ComTyp.ZAEHLZEITSAISON

    bezeichnung: Optional[str] = None
    """Bezeichnung der Saison (z.B. "Sommer", "Winter"). Muss zu einem Saisonabschnitt des in der
    übergeordneten `Zaehlzeitdefinition` referenzierten `saisonprofil` passen. Leer, wenn keine
    Saisonunterscheidung getroffen wird."""
    tagtypen: Optional[list["Zaehlzeittagtyp"]] = None
    """Die Schaltschemata für die unterschiedlichen Tagtypen (z.B. Werktag, Wochenende, Feiertag)
    innerhalb dieser Saison."""
