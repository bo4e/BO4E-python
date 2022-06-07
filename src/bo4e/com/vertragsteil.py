"""
Contains Vertragsteil class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attrs
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Vertragsteil(COM):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/VertragsteilSchema.json>`_

    """

    # required attributes
    vertragsteilbeginn: datetime = attrs.field(validator=attrs.validators.instance_of(datetime))
    """
    Start der Gültigkeit des Vertragsteils (inklusiv)
    """
    vertragsteilende: datetime = attrs.field(validator=attrs.validators.instance_of(datetime))
    """
    Ende der Gültigkeit des Vertragsteils (exklusiv)
    """

    # optional attributes
    lokation: Optional[str] = attrs.field(default=None)
    """
    Der Identifier für diejenigen Markt- oder Messlokation, die zu diesem Vertragsteil gehören.
    Verträge für mehrere Lokationen werden mit mehreren Vertragsteilen abgebildet
    """
    vertraglich_fixierte_menge: Optional[Menge] = attrs.field(default=None)
    """
    Für die Lokation festgeschriebene Abnahmemenge
    """
    minimale_abnahmemenge: Optional[Menge] = attrs.field(default=None)
    """
    Für die Lokation festgelegte Mindestabnahmemenge (inklusiv)
    """
    maximale_abnahmemenge: Optional[Menge] = attrs.field(default=None)
    """
    Für die Lokation festgelegte maximale Abnahmemenge (exklusiv)
    """


class VertragsteilSchema(COMSchema):
    """
    Schema for de-/serialization of Vertragsteil.
    """

    class_name = Vertragsteil
    # required attributes
    vertragsteilbeginn = fields.DateTime()
    vertragsteilende = fields.DateTime()

    # optional attributes
    lokation = fields.String(load_default=None)
    vertraglich_fixierte_menge = fields.Nested(MengeSchema, load_default=None, data_key="vertraglichFixierteMenge")
    minimale_abnahmemenge = fields.Nested(MengeSchema, load_default=None, data_key="minimaleAbnahmemenge")
    maximale_abnahmemenge = fields.Nested(MengeSchema, load_default=None, data_key="maximaleAbnahmemenge")
