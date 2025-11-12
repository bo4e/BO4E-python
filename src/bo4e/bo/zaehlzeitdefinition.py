"""
Contains Zaehlzeitdefinition class
"""

# pylint: disable=unused-argument
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.umschaltzeit import Umschaltzeit
    from ..enum.wiederholungstyp import Wiederholungstyp

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Zaehlzeitdefinition(Geschaeftsobjekt):
    """
    Beinhaltet Informationen zu welchen Zeiten welche Register zählen.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Zaehlzeitdefinition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zaehlzeitdefinition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Zaehlzeitdefinition.json>`_

    """

    typ: Annotated[Literal[BoTyp.ZAEHLZEITDEFINITION], Field(alias="_typ")] = BoTyp.ZAEHLZEITDEFINITION

    wiederholend: Optional["Wiederholungstyp"] = None
    """Dieses Feld gibt an, an welchen Tagen das Schaltschema gilt, das durch die Umschaltzeiten definiert ist."""
    umschaltzeiten: Optional[list["Umschaltzeit"]] = None
    """
    Die einzelnen Umschaltzeiten in dieser Liste definieren, zu welchen Uhrzeiten welches Register zählt.

    Die Liste füllt stets einen ganzen Tag vollständig und überlappungsfrei aus. Die jeweilige Umschaltzeit in jedem
    Objekt der Liste ergibt (wenn der Größe nach sortiert) ein entsprechendes Schema, wobei die untere Grenze (inklusiv)
    als 00:00 Uhr und die obere Grenze (exklusiv) als 24:00 Uhr definiert ist.

    Anmerkung: Die Umschaltzeiten sollten sich natürlich niemals doppeln.
    """
