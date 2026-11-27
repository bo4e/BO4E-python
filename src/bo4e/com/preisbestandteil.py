"""
Contains Preisbestandteil class
"""

from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..bo.preisblatt import Preisblatt
    from ..bo.preisblattkonzessionsabgabe import PreisblattKonzessionsabgabe
    from ..bo.preisblattmessung import PreisblattMessung
    from ..bo.preisblattnetznutzung import PreisblattNetznutzung


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Preisbestandteil(COM):
    """
    Komponente zur Abbildung von Preisbestandteilen.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Preisbestandteil.svg" type="image/svg+xml"></object>

    .. HINT::
        `Preisbestandteil JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Preisbestandteil.json>`_

    """

    typ: Annotated[Literal[ComTyp.PREISBESTANDTEIL], Field(alias="_typ")] = ComTyp.PREISBESTANDTEIL

    steuern_umlagen: list["Preisblatt"] | None = None
    """Auflistung der `Steuern und Umlagen`, die im Preis einberechnet wurden."""
    netznutzung: list["PreisblattNetznutzung"] | None = None
    """Auflistung der `Netznutzungspreise`, die im Preis einberechnet wurden."""
    messung: list["PreisblattMessung"] | None = None
    """Auflistung der `Messpreise`, die im Preis einberechnet wurden."""
    konzessionsabgabe: list["PreisblattKonzessionsabgabe"] | None = None
    """Auflistung der `Konzessionsabgaben`, die im Preis einberechnet wurden."""
