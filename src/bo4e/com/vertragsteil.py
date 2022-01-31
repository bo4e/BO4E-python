"""
Contains Vertragsteil class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attr
from marshmallow import fields

from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Vertragsteil(COM):
    """
    Abbildung für einen Vertragsteil. Der Vertragsteil wird dazu verwendet,
    eine vertragliche Leistung in Bezug zu einer Lokation (Markt- oder Messlokation) festzulegen.

    .. HINT::
        `Vertragsteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/master/json_schemas/com/VertragsteilSchema.json>`_

    """

    # required attributes
    vertragsteilbeginn: datetime = attr.ib(validator=attr.validators.instance_of(datetime))
    vertragsteilende: datetime = attr.ib(validator=attr.validators.instance_of(datetime))

    # optional attributes
    lokation: Optional[str] = attr.ib(default=None)
    vertraglich_fixierte_menge: Optional[Menge] = attr.ib(default=None)
    minimale_abnahmemenge: Optional[Menge] = attr.ib(default=None)
    maximale_abnahmemenge: Optional[Menge] = attr.ib(default=None)


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
