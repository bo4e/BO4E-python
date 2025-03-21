"""
Contains Zeitraum class
"""

from datetime import date, time
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.mengeneinheit import Mengeneinheit


# pylint: disable=too-few-public-methods
@postprocess_docstring
class Zeitraum(COM):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zeitraum.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zeitraum JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zeitraum.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZEITRAUM], Field(alias="_typ")] = ComTyp.ZEITRAUM

    startdatum: Optional[date] = None
    """Startdatum des betrachteten Zeitraums ist **inklusiv**.

    Example:
        '2025-01-01'
    """
    enddatum: Optional[date] = None
    """Enddatum des betrachteten Zeitraums ist **inklusiv**.

    Example:
        '2025-01-01'
    """
    startuhrzeit: Optional[time] = None
    """Startuhrzeit mit Zeitzone. Die angegebene Uhrzeit ist im betrachteten Zeitraum **inklusiv**.

    Example:
        '18:00:00+01:00'
    """
    enduhrzeit: Optional[time] = None
    """Enduhrzeit mit Zeitzone. Die angegebene Uhrzeit ist im betrachteten Zeitraum **exklusiv**.

    Example:
        '19:00:00+01:00'
    """
    dauer: Optional[str] = None
    """
    Dauer in ISO 8601 Format.

    Example:
        'P1DT30H4S'

    See `RFC 3339 <https://datatracker.ietf.org/doc/html/rfc3339>`_
    """
