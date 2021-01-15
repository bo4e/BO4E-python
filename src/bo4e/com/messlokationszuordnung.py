import attr

from datetime import datetime
from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

from bo4e.cases import JavaScriptMixin
from bo4e.com.com import COM
from bo4e.enum.arithmetische_operation import ArithmetischeOperation


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


class MesslokationszuordnungSchema(Schema, JavaScriptMixin):
    # required attributes
    messlokations_id = fields.Str()
    arithmetik = EnumField(ArithmetischeOperation)

    # optional attributes
    gueltig_seit = fields.DateTime(missing=None)
    gueltig_bis = fields.DateTime(missing=None)

    @post_load
    def deserialise(self, data, **kwargs) -> Messlokationszuordnung:
        return Messlokationszuordnung(**data)
