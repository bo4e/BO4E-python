"""
Contains PositionsAufAbschlag and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

from bo4e.com.com import COM
from bo4e.enum.waehrungseinheit import Waehrungseinheit

# pylint: disable=too-few-public-methods


class PositionsAufAbschlag(COM):
    """
    Differenzierung der zu betrachtenden Produkte anhand der preiserhöhenden (Aufschlag)
    bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen werden können.
    Es können mehrere Auf-/Abschläge gleichzeitig ausgewählt werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/PositionsAufAbschlag.svg" type="image/svg+xml"></object>

    .. HINT::
        `PositionsAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PositionsAufAbschlag.json>`_

    """

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: str
    #: Typ des AufAbschlages
    auf_abschlagstyp: str
    #: Höhe des Auf-/Abschlages
    auf_abschlagswert: Decimal
    #: Einheit, in der der Auf-/Abschlag angegeben ist (z.B. ct/kWh).
    auf_abschlagswaehrung: Waehrungseinheit
