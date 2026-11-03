"""
Contains Tarifeinschraenkung
"""

from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.zaehlertyp import Zaehlertyp
    from .menge import Menge

# pylint: disable=too-few-public-methods


@postprocess_docstring
class Tarifeinschraenkung(COM):
    """
    Mit dieser Komponente werden Einschränkungen für die Anwendung von Tarifen modelliert.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifeinschraenkung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifeinschraenkung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarifeinschraenkung.json>`_

    """

    typ: Annotated[Literal[ComTyp.TARIFEINSCHRAENKUNG], Field(alias="_typ")] = ComTyp.TARIFEINSCHRAENKUNG

    zusatzprodukte: list[str] | None = None
    """Weitere Produkte, die gemeinsam mit diesem Tarif bestellt werden können"""
    einschraenkungzaehler: list["Zaehlertyp"] | None = None
    einschraenkungleistung: list["Menge"] | None = None
    """ Die vereinbarte Leistung, die (näherungsweise) abgenommen wird.
    Insbesondere Gastarife können daran gebunden sein, dass die Leistung einer vereinbarten Höhe entspricht. """
