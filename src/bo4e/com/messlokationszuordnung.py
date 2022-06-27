"""
Contains Messlokationszuordnung class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime

from bo4e.com.com import COM
from bo4e.enum.arithmetische_operation import ArithmetischeOperation


# pylint: disable=too-few-public-methods


class Messlokationszuordnung(COM):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.

    .. graphviz:: /api/dots/bo4e/com/Messlokationszuordnung.dot

    """

    # required attributes
    messlokations_id: str
    arithmetik: ArithmetischeOperation

    # optional attributes
    gueltig_seit: datetime = None
    gueltig_bis: datetime = None
