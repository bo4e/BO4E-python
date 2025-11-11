"""
Contains Verbrauch
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit
    from ..enum.messwertstatus import Messwertstatus


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

    typ: Annotated[Literal[ComTyp.VERBRAUCH], Field(alias="_typ")] = ComTyp.VERBRAUCH

    obis_kennzahl: Optional[str] = None
    """Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:"""
    wert: Optional[Decimal] = None
    """Gibt den absoluten Wert der Menge an"""
    einheit: Optional["Mengeneinheit"] = None
    """Gibt die Einheit zum jeweiligen Wert an"""

    startdatum: Optional[pydantic.AwareDatetime] = None
    """Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird"""
    enddatum: Optional[pydantic.AwareDatetime] = None
    """
    Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird.
    Ein ZeitPUNKT kann mit start==ende angegeben werden.
    """
    messwertstatus: Optional["Messwertstatus"] = None
    """Messwertstatus includes the plausibility of the value"""
