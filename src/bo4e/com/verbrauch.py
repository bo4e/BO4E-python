"""
Contains Verbrauch and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional

from ..enum.mengeneinheit import Mengeneinheit
from ..enum.messwertstatus import Messwertstatus
from ..enum.wertermittlungsverfahren import Wertermittlungsverfahren
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Verbrauch(COM):
    """
    Abbildung eines zeitlich abgegrenzten Verbrauchs

    .. raw:: html

        <object data="../_static/images/bo4e/com/Verbrauch.svg" type="image/svg+xml"></object>

    .. HINT::
        `Verbrauch JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Verbrauch.json>`_

    """

    #: Gibt an, ob es sich um eine PROGNOSE oder eine MESSUNG handelt
    wertermittlungsverfahren: Optional[Wertermittlungsverfahren] = None
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:
    obis_kennzahl: Optional[str] = None
    #: Gibt den absoluten Wert der Menge an
    wert: Optional[Decimal] = None
    #: Gibt die Einheit zum jeweiligen Wert an
    einheit: Optional[Mengeneinheit] = None

    #: Inklusiver Beginn des Zeitraumes, für den der Verbrauch angegeben wird
    startdatum: Optional[datetime] = None
    #: Exklusives Ende des Zeitraumes, für den der Verbrauch angegeben wird
    enddatum: Optional[datetime] = None
    #: Messwertstatus includes the plausibility of the value
    messwertstatus: Optional[Messwertstatus] = None
