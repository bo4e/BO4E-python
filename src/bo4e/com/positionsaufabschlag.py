"""
Contains PositionsAufAbschlag and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class PositionsAufAbschlag(COM):
    """
    Differenzierung der zu betrachtenden Produkte anhand der preiserhöhenden (Aufschlag)
    bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen werden können.
    Es können mehrere Auf-/Abschläge gleichzeitig ausgewählt werden.

    .. HINT::
        `PositionsAufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PositionsAufAbschlagSchema.json>`_

    """

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Typ des AufAbschlages
    auf_abschlagstyp: str = attrs.field(validator=attrs.validators.instance_of(AufAbschlagstyp))
    #: Höhe des Auf-/Abschlages
    auf_abschlagswert: Decimal = attrs.field(validator=attrs.validators.instance_of(Decimal))
    #: Einheit, in der der Auf-/Abschlag angegeben ist (z.B. ct/kWh).
    auf_abschlagswaehrung: Waehrungseinheit = attrs.field(validator=attrs.validators.instance_of(Waehrungseinheit))


class PositionsAufAbschlagSchema(COMSchema):
    """
    Schema for de-/serialization of PositionsAufAbschlag
    """

    class_name = PositionsAufAbschlag
    # required attributes
    bezeichnung = fields.Str()
    beschreibung = fields.Str()
    auf_abschlagstyp = EnumField(AufAbschlagstyp, data_key="aufAbschlagstyp")
    auf_abschlagswert = fields.Decimal(as_string=True, data_key="aufAbschlagswert")
    auf_abschlagswaehrung = EnumField(Waehrungseinheit, data_key="aufAbschlagswaehrung")
