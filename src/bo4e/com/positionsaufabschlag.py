"""
Contains PositionsAufAbschlag and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal

# pylint: disable=too-few-public-methods
from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.aufabschlagstyp import AufAbschlagstyp
    from ..enum.waehrungseinheit import Waehrungseinheit


@postprocess_docstring
class PositionsAufAbschlag(COM):
    """
    Differenzierung der zu betrachtenden Produkte anhand der preiserhöhenden (Aufschlag)
    bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen werden können.
    Es können mehrere Auf-/Abschläge gleichzeitig ausgewählt werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/PositionsAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `PositionsAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/PositionsAufAbschlag.json>`_

    """

    bezeichnung: Optional[str] = None
    """Bezeichnung des Auf-/Abschlags"""
    beschreibung: Optional[str] = None
    """Beschreibung zum Auf-/Abschlag"""
    auf_abschlagstyp: Optional["AufAbschlagstyp"] = None
    """Typ des AufAbschlages"""
    auf_abschlagswert: Optional[Decimal] = None
    """Höhe des Auf-/Abschlages"""
    auf_abschlagswaehrung: Optional["Waehrungseinheit"] = None
    """Einheit, in der der Auf-/Abschlag angegeben ist (z.B. ct/kWh)."""
