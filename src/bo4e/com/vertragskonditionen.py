"""
Contains Vertragskonditionen class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Vertragskonditionen(COM):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.

    .. HINT::
        `Vertragskonditionen JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/VertragskonditionenSchema.json>`_

    """

    # optional attributes
    beschreibung: str = attr.ib(default=None)
    anzahl_abschlaege: Decimal = attr.ib(default=None)
    vertragslaufzeit: Zeitraum = attr.ib(default=None)
    kuendigungsfrist: Zeitraum = attr.ib(default=None)
    vertragsverlaengerung: Zeitraum = attr.ib(default=None)
    abschlagszyklus: Zeitraum = attr.ib(default=None)


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
