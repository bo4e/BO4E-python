"""
Contains Kostenblock
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .betrag import Betrag
    from .kostenposition import Kostenposition

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Kostenblock(COM):
    """
    Mit dieser Komponente werden mehrere Kostenpositionen zusammengefasst.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kostenblock.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kostenblock JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Kostenblock.json>`_

    """

    typ: Annotated[Literal[ComTyp.KOSTENBLOCK], Field(alias="_typ")] = ComTyp.KOSTENBLOCK

    kostenblockbezeichnung: Optional[str] = None
    """Bezeichnung für einen Kostenblock. Z.B. Netzkosten, Messkosten, Umlagen, etc."""

    summe_kostenblock: Optional["Betrag"] = None
    """Die Summe aller Kostenpositionen dieses Blocks"""

    kostenpositionen: Optional[list["Kostenposition"]] = None
    """
    Hier sind die Details zu einer Kostenposition aufgeführt. Z.B.:
    Alliander Netz Heinsberg GmbH, 01.02.2018, 31.12.2018, Arbeitspreis HT, 3.660 kWh, 5,8200 ct/kWh, 213,01 €
    """
