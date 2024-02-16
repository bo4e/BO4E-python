"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import Optional

import pydantic

from ..enum.mengeneinheit import Mengeneinheit
from ..utils import postprocess_docstring
from .com import COM

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

    einheit: Optional[Mengeneinheit] = None
    dauer: Optional[Decimal] = None
    startdatum: Optional[pydantic.AwareDatetime] = None
    enddatum: Optional[pydantic.AwareDatetime] = None
    startzeitpunkt: Optional[pydantic.AwareDatetime] = None
    endzeitpunkt: Optional[pydantic.AwareDatetime] = None
