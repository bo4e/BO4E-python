"""
Contains Messlokationszuordnung class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

from pydantic import StrictStr

from bo4e.com.com import COM
from bo4e.enum.arithmetische_operation import ArithmetischeOperation


# pylint: disable=too-few-public-methods


class Messlokationszuordnung(COM):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.

    .. HINT::
        `Messlokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/MesslokationszuordnungSchema.json>`_

    """

    # required attributes
    messlokations_id: str
    arithmetik: ArithmetischeOperation

    # optional attributes
    gueltig_seit: datetime = None
    gueltig_bis: datetime = None
