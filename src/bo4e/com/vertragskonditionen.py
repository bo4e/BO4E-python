"""
Contains Vertragskonditionen class
and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal

import attr
from marshmallow import fields, post_load

from bo4e.com.com import COM, COMSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Vertragskonditionen(COM):
    """
    Abbildung für Vertragskonditionen. Die Komponente wird sowohl im Vertrag als auch im Tarif verwendet.
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

    # optional attributes
    beschreibung = fields.String(load_default=None)
    anzahl_abschlaege = fields.Decimal(load_default=None, as_string=True)
    vertragslaufzeit = fields.Nested(ZeitraumSchema, load_default=None)
    kuendigungsfrist = fields.Nested(ZeitraumSchema, load_default=None)
    vertragsverlaengerung = fields.Nested(ZeitraumSchema, load_default=None)
    abschlagszyklus = fields.Nested(ZeitraumSchema, load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Vertragskonditionen:
        """Deserialize JSON to Vertragskonditionen object"""
        return Vertragskonditionen(**data)
