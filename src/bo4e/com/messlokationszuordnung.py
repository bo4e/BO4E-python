"""
Contains Messlokationszuordnung class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

import pydantic

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.arithmetische_operation import ArithmetischeOperation


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Messlokationszuordnung(COM):
    """
    Mit dieser Komponente werden Messlokationen zu Marktlokationen zugeordnet.
    Dabei kann eine arithmetische Operation (Addition, Subtraktion, Multiplikation, Division) angegeben werden,
    mit der die Messlokation zum Verbrauch der Marktlokation beiträgt.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Messlokationszuordnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Messlokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Messlokationszuordnung.json>`_

    """

    messlokations_id: Optional[str] = None
    """
    ID der zugeordneten Messlokation
    """
    arithmetik: Optional["ArithmetischeOperation"] = None

    gueltig_seit: Optional[pydantic.AwareDatetime] = None
    """
    inklusives Beginndatum
    """
    gueltig_bis: Optional[pydantic.AwareDatetime] = None
    """
    exklusives Endedatum
    """
