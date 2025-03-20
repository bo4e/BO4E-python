"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from datetime import date, time
from typing import TYPE_CHECKING, Optional

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

    startdatum: Optional[date] = None
    """Startdatum, inklusiv"""
    enddatum: Optional[date] = None
    """Enddatum, inklusiv"""
    startuhrzeit: Optional[time] = None
    """Startuhrzeit, inklusiv mit Zeitzone"""
    enduhrzeit: Optional[time] = None
    """Enduhrzeit, exklusiv mit Zeitzone"""
    dauer: Optional[str] = None
    """
    Dauer in ISO 8601 Format.

    Example:
        'P1DT30H4S'

    See `RFC 3339 <https://datatracker.ietf.org/doc/html/rfc3339>`_
    """
