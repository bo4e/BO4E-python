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
    iban: Optional[str] = None
    """Eine IBAN-Nummer"""
    bic: Optional[str] = None
    """Eine BIC-Nummer"""
    kontoinhaber: Optional[str] = None
    """Der Name des Kontoinhabers"""
    betreff: Optional[str] = None
    """Eine konstante Betreffzeile für Überweisungen"""
    sepa_referenz: Optional[str] = None
    """Eine SEPA-Referenz"""
