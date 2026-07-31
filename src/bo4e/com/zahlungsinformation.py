"""
Contains Zahlungsinformation class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.zahlungsart import Zahlungsart


@postprocess_docstring
class Zahlungsinformation(COM):
    """
    Mit dieser Komponente kann eine einzelne Zahlungsinformation dargestellt werden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Zahlungsinformation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Zahlungsinformation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Zahlungsinformation.json>`_

    """

    typ: Annotated[Literal[ComTyp.ZAHLUNGSINFORMATION], Field(alias="_typ")] = ComTyp.ZAHLUNGSINFORMATION

    zahlungsart: Optional["Zahlungsart"] = None
    """Die Zahlungsart dieser Zahlungsinformation"""
    iban: str | None = None
    """Eine IBAN-Nummer"""
    bic: str | None = None
    """Eine BIC-Nummer"""
    kontoinhaber: str | None = None
    """Der Name des Kontoinhabers"""
    betreff: str | None = None
    """Eine konstante Betreffzeile für Überweisungen"""
    sepa_referenz: str | None = None
    """Eine SEPA-Referenz"""
