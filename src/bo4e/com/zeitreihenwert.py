"""
Contains Zeitreihenwert class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..com.zeitraum import Zeitraum
    from ..enum.messwertstatus import Messwertstatus
    from ..enum.messwertstatuszusatz import Messwertstatuszusatz


# pylint: disable=too-few-public-methods
@postprocess_docstring
class Zeitreihenwert(COM):
    """
    Abbildung eines Zeitreihenwertes bestehend aus Zeitraum, Wert und Statusinformationen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitreihenwert.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitreihenwert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zeitreihenwert.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZEITREIHENWERT], Field(alias="_typ")] = ComTyp.ZEITREIHENWERT

    zeitraum: Optional["Zeitraum"] = None
    """Zeitraum für das Messintervall"""
    wert: Optional[Decimal] = None
    """Der in dem Zeitraum gültige Wert."""
    status: Optional["Messwertstatus"] = None
    """Der Status gibt an, wie der Wert zu interpretieren ist, z.B. in Berechnungen."""
    statuszusatz: Optional["Messwertstatuszusatz"] = None
    """Eine Zusatzinformation zum Status, beispielsweise ein Grund für einen fehlenden Wert."""
