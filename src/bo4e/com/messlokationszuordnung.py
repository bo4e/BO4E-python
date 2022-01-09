"""
Contains Messlokationszuordnung class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.arithmetische_operation import ArithmetischeOperation


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Messlokationszuordnung(COM):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.
    """

    # required attributes
    messlokations_id: str
    arithmetik: ArithmetischeOperation

    # optional attributes
    gueltig_seit: datetime = attr.ib(default=None)
    gueltig_bis: datetime = attr.ib(default=None)


class MesslokationszuordnungSchema(COMSchema):
    """
    Schema for de-/serialization of Katasteradresse.
    """

    class_name = Messlokationszuordnung
    # required attributes
    messlokations_id = fields.Str()
    arithmetik = EnumField(ArithmetischeOperation)

    # optional attributes
    gueltig_seit = fields.DateTime(load_default=None)
    gueltig_bis = fields.DateTime(load_default=None)
