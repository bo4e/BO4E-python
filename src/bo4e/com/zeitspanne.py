"""
contains the COM Zeitspanne
"""

from datetime import date, time
from typing import Optional

from bo4e.com.com import COM

from ..utils import postprocess_docstring


@postprocess_docstring
class Zeitspanne(COM):
    """
    Eine Zeitspanne ist definiert aus Start- und Enddatum sowie Start- und Enduhrzeit.
    Der Unterschied zur Menge (die auch zur Abbildung von Zeitmengen genutzt wird) ist, dass konkrete Start- und Endzeitpunkte angegeben werden.
    Die Zeitspanne ist aus dem COM Zeitraum hervorgegangen, das in Zeitspanne und Menge aufgeteilt wurde.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitspanne.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitspanne JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zeitspanne.json>`_

    """

    #: start and ende will be removed
    # start: Optional[pydantic.AwareDatetime] = None  #: inklusiver Beginn
    # ende: Optional[pydantic.AwareDatetime] = None  #: exklusives Ende
    startdatum: Optional[date] = None  #: inklusiver Beginn
    enddatum: Optional[date] = None  #: inklusives Ende
    startuhrzeit: Optional[time] = None  #: inklusiver Beginn
    enduhrzeit: Optional[time] = None  #: exklusives Ende
