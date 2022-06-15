"""
Contains Vertragskonditionen class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Vertragskonditionen(COM):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/VertragskonditionenSchema.json>`_

    """

    # optional attributes
    #: Freitext zur Beschreibung der Konditionen, z.B. "Standardkonditionen Gas"
    beschreibung: str = attrs.field(default=None)
    #: Anzahl der vereinbarten Abschläge pro Jahr, z.B. 12
    anzahl_abschlaege: Decimal = attrs.field(default=None)
    #: Über diesen Zeitraum läuft der Vertrag
    vertragslaufzeit: Zeitraum = attrs.field(default=None)
    #: Innerhalb dieser Frist kann der Vertrag gekündigt werden
    kuendigungsfrist: Zeitraum = attrs.field(default=None)
    #: Falls der Vertrag nicht gekündigt wird, verlängert er sich automatisch um die hier angegebene Zeit
    vertragsverlaengerung: Zeitraum = attrs.field(default=None)
    #: In diesen Zyklen werden Abschläge gestellt. Alternativ kann auch die Anzahl in den Konditionen angeben werden.
    abschlagszyklus: Zeitraum = attrs.field(default=None)


class VertragskonditionenSchema(COMSchema):
    """
    Schema for de-/serialization of Vertragskonditionen.
    """

    class_name = Vertragskonditionen
    # optional attributes
    beschreibung = fields.String(load_default=None)
    anzahl_abschlaege = fields.Decimal(load_default=None, as_string=True, data_key="anzahlAbschlaege")
    vertragslaufzeit = fields.Nested(ZeitraumSchema, load_default=None)
    kuendigungsfrist = fields.Nested(ZeitraumSchema, load_default=None)
    vertragsverlaengerung = fields.Nested(ZeitraumSchema, load_default=None)
    abschlagszyklus = fields.Nested(ZeitraumSchema, load_default=None)
