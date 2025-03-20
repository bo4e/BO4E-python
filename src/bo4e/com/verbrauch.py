"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Optional

import pydantic

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.messwertstatus import Messwertstatus
    from ..enum.wertermittlungsverfahren import Wertermittlungsverfahren


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Verbrauch(COM):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verbrauch.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Verbrauch.json>`_

    """

    wertermittlungsverfahren: Optional["Wertermittlungsverfahren"] = None
    """Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt"""
    obis_kennzahl: Optional[str] = None
    """Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:"""
    wert: Optional[Decimal] = None
    """Gibt den absoluten Wert der Menge an"""
    einheit: Optional["Mengeneinheit"] = None
    """Gibt die Einheit zum jeweiligen Wert an"""

    startdatum: Optional[pydantic.AwareDatetime] = None
    """Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird"""
    enddatum: Optional[pydantic.AwareDatetime] = None
    """Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird"""
    messwertstatus: Optional["Messwertstatus"] = None
    """Messwertstatus includes the plausibility of the value"""
