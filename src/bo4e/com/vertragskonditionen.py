"""
Contains Vertragskonditionen class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Vertragskonditionen(COM):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragskonditionen.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Vertragskonditionen.json>`_

    """

    beschreibung: Optional[str] = None
    """
    Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas"
    """
    anzahl_abschlaege: Optional[Decimal] = None
    """Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12"""
    vertragslaufzeit: Optional["Zeitraum"] = None
    """Über diesen Zeitraum läuft der Vertrag"""
    kuendigungsfrist: Optional["Zeitraum"] = None
    """Innerhalb dieser Frist kann der Vertrag gekündigt werden"""
    vertragsverlaengerung: Optional["Zeitraum"] = None
    """Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit"""
    abschlagszyklus: Optional["Zeitraum"] = None
    """In diesen Zyklen werden Abschläge gestellt. Alternativ kann auch die Anzahl in den Konditionen angeben werden."""
