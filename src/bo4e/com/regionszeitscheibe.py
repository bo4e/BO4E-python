"""
Contains Regionszeitscheibe class
"""

from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..bo.region import Region
    from .zeitraum import Zeitraum


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Regionszeitscheibe(COM):
    """
    Komponente zur Abbildung einer Region mit einer Zeitscheibe.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Regionszeitscheibe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Regionszeitscheibe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Regionszeitscheibe.json>`_

    """

    typ: Annotated[Literal[ComTyp.REGIONSZEITSCHEIBE], Field(alias="_typ")] = ComTyp.REGIONSZEITSCHEIBE

    region: Optional["Region"] = None
    """Die Region wird durch das Feld `zeitscheibengueltigkeit ` mit einer Zeitscheibe versehen."""
    zeitscheibengueltigkeit: Optional["Zeitraum"] = None
    """
    Versieht die Region mit einer Zeitscheibe. Der Start- und Endzeitpunkt sollte durch das Objekt ermittelbar sein.
    """
