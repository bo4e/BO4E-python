"""
Contains Messlokationszuordnung class
and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

from bo4e.com.com import COM
from bo4e.enum.arithmetische_operation import ArithmetischeOperation

# pylint: disable=too-few-public-methods


class Messlokationszuordnung(COM):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Messlokationszuordnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Messlokationszuordnung.json>`_

    """

    # required attributes
    messlokations_id: str
    """
    ID der zugeordneten Messlokation
    """
    arithmetik: ArithmetischeOperation

    # optional attributes
    gueltig_seit: Optional[datetime] = None
    """
    inklusives Beginndatum
    """
    gueltig_bis: Optional[datetime] = None
    """
    exklusives Endedatum
    """
