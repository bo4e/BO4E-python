"""
Contains PositionsAufAbschlag and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

# pylint: disable=too-few-public-methods
from ..enum.aufabschlagstyp import AufAbschlagstyp
from ..enum.waehrungseinheit import Waehrungseinheit
from ..utils import postprocess_docstring
from .com import COM


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
        `PositionsAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/PositionsAufAbschlag.json>`_

    """

    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: Optional[str] = None
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: Optional[str] = None
    #: Typ des AufAbschlages
    auf_abschlagstyp: Optional[AufAbschlagstyp] = None
    #: Höhe des Auf-/Abschlages
    auf_abschlagswert: Optional[Decimal] = None
    #: Einheit, in der der Auf-/Abschlag angegeben ist (z.B. ct/kWh).
    auf_abschlagswaehrung: Optional[Waehrungseinheit] = None
