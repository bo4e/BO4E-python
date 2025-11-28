"""
Contains Tarifpreiszeitscheibe class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from .einheitspreisposition import EinheitsPreisposition
    from .lastvariablepreisposition import LastvariablePreisposition
    from .relativepreisposition import RelativePreisposition
    from .zeitraum import Zeitraum
    from .zeitvariablepreisposition import ZeitvariablePreisposition


@postprocess_docstring
class Tarifpreiszeitscheibe(COM):
    """
    Mit dieser Komponente kann ein aus verschiedenen Preispositionen zusammengesetzter Tarifpreis zeitaufgelöst
    dargestellt werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreiszeitscheibe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreiszeitscheibe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarifpreiszeitscheibe.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIFPREISZEITSCHEIBE], Field(alias="_typ")] = ComTyp.TARIFPREISZEITSCHEIBE

    zeitscheibengueltigkeit: Optional["Zeitraum"] = None
    """Gibt an für welchen Zeitraum dieser zusammengesetzte Tarifpreis gültig ist."""
    einheits_preispositionen: Optional[list["EinheitsPreisposition"]] = None
    """Eine Liste von Einheits-Preispositionen."""
    zeitvariable_preispositionen: Optional[list["ZeitvariablePreisposition"]] = None
    """
    Eine Liste von zeitvariablen Preispositionen.
    Dies können z.B. Preispositionen mit Zählzeitdefinitionen sein, um ein klassisches HT/NT Modell abzubilden.
    """
    lastvariable_preispositionen: Optional[list["LastvariablePreisposition"]] = None
    """
    Eine Liste von lastvariablen Preispositionen.
    Diese Preispositionen sind vorgesehen, um bspw. ein Staffel- oder Zonenmodell abzubilden.
    """
    relative_preispositionen: Optional[list["RelativePreisposition"]] = None
    """
    Eine Liste von relativen Preispositionen.
    Diese Preispositionen modellieren prozentuale Modifikationen auf bestehende Preispositionen.

    Dazu wird über ein Feld in `RelativePreisposition` auf die `_id` einer anderen Preispositionen verwiesen.
    Die ID hat hierbei kein vorgegebenes Format und hat auch keine fachliche Bedeutung. Es handelt sich hierbei
    um eine rein technische Lösung, um einen Querverweis zu modellieren.
    """
    dynamischer_tarif_quelle: Optional[str] = None
    """Gibt die Bezugsquelle für den dynamischen Tarif an. TODO: Brauchen wir das hier überhaupt noch???"""
