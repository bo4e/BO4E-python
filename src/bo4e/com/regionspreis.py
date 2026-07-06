"""
Contains Regionspreis class
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from .regionszeitscheibe import Regionszeitscheibe
    from .tarifpreiszeitscheibe import Tarifpreiszeitscheibe


@postprocess_docstring
class Regionspreis(COM):
    """
    Mit dieser Komponente wird ein aus mehreren Positionen zusammengesetzter Preis regionsaufgelöst dargestellt.
    Zu jedem Zeitpunkt darf es nur eine gültige Region und einen gültigen Preis geben.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Regionspreis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionspreis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Regionspreis.json>`_

    """

    typ: Annotated[Literal[ComTyp.REGIONSPREIS], Field(alias="_typ")] = ComTyp.REGIONSPREIS

    regionszeitscheiben: Optional[list["Regionszeitscheibe"]] = None
    """
    Eine Liste von mit Zeitscheiben versehenen Regionen.
    Die Zeitscheiben sollten sich nicht überschneiden.
    """
    tarifpreiszeitscheiben: Optional[list["Tarifpreiszeitscheibe"]] = None
    """
    Eine Liste von mit Zeitscheiben versehenen Tarifpreisen.
    Die Zeitscheiben sollten sich nicht überschneiden.
    Die Tarifpreise sind aus mehreren Tarifpreispositionen zusammengesetzt.
    """
