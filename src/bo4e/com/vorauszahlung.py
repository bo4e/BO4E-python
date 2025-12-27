"""
Contains Vorauszahlung class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import AwareDatetime, Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from .betrag import Betrag


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Vorauszahlung(COM):
    """
    Dient zur Identifizierung eines vorausgezahlten Betrags.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Vorauszahlung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Vorauszahlung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Vorauszahlung.json>`_

    """

    typ: Annotated[Literal[ComTyp.VORAUSZAHLUNG], Field(alias="_typ")] = ComTyp.VORAUSZAHLUNG

    betrag: Optional["Betrag"] = None
    datum: Optional[AwareDatetime] = None
    referenz: Optional[str] = None
