"""
Contains Zeitraum class
and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional
from decimal import Decimal
from datetime import date, datetime

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField

from bo4e.com.com import COM, COMSchema
from bo4e.enum.zeiteinheit import Zeiteinheit

# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Zeitraum(COM):
    """
    Diese Komponente wird zur Abbildung von Zeiträumen in Form von Dauern oder der Angabe von Start und Ende verwendet.
    Es muss daher eine der drei Möglichkeiten angegeben sein:
    - Einheit und Dauer oder
    - Zeitraum: Startdatum bis Enddatum oder
    - Zeitraum: Startzeitpunkt (Datum und Uhrzeit) bis Endzeitpunkt (Datum und Uhrzeit)
    """

    # optional attributes
    einheit: Optional[Zeiteinheit] = attr.ib(default=None)
    dauer: Optional[Decimal] = attr.ib(default=None)
    startdatum: Optional[date] = attr.ib(default=None)
    enddatum: Optional[date] = attr.ib(default=None)
    startzeitpunkt: Optional[datetime] = attr.ib(default=None)
    endzeitpunkt: Optional[datetime] = attr.ib(default=None)


class ZeitraumSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitraum.
    """

    # optional attributes
    einheit = EnumField(Zeiteinheit, missing=None)
    dauer = fields.Decimal(missing=None, as_string=True)
    startdatum = fields.Date(missing=None)
    enddatum = fields.Date(missing=None)
    startzeitpunkt = fields.DateTime(missing=None)
    endzeitpunkt = fields.DateTime(missing=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Zeitraum:
        """Deserialize JSON to Zeitraum object"""
        return Zeitraum(**data)
