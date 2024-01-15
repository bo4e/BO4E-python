"""
Contains Vertragskonditionen class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from ..utils import postprocess_docstring
from .com import COM
from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Vertragskonditionen(COM):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vertragskonditionen.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Vertragskonditionen.json>`_

    """

    #: Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas"
    beschreibung: Optional[str] = None
    #: Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12
    anzahl_abschlaege: Optional[Decimal] = None
    #: Über diesen Zeitraum läuft der Vertrag
    vertragslaufzeit: Optional[Zeitraum] = None
    #: Innerhalb dieser Frist kann der Vertrag gekündigt werden
    kuendigungsfrist: Optional[Zeitraum] = None
    #: Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit
    vertragsverlaengerung: Optional[Zeitraum] = None
    #: In diesen Zyklen werden Abschläge gestellt. Alternativ kann auch die Anzahl in den Konditionen angeben werden.
    abschlagszyklus: Optional[Zeitraum] = None
