"""
Contains RelativePreisposition class
"""

from decimal import Decimal

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM


@postprocess_docstring
class RelativePreisposition(COM):
    """
    Modelliert eine relative Preisposition.

    .. raw:: html

        <object data="../_static/images/bo4e/com/RelativePreisposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `RelativePreisposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/RelativePreisposition.json>`_

    """

    typ: Annotated[Literal[ComTyp.RELATIVEPREISPOSITION], Field(alias="_typ")] = ComTyp.RELATIVEPREISPOSITION

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für die Preisposition."""
    id_referenz: Optional[str] = None
    """
    Referenziert auf eine andere Preisposition.
    Die Referenz bezieht sich auf das technische Feld `_id`, da es sich hier um eine technische Lösung handelt
    und der Wert selbst keine fachliche Bedeutung hat.
    Das `_id` Feld der unterschiedlichen Preispositionen muss innerhalb einer `Tarifpreiszeitscheibe`
    entsprechend unique sein.
    """
    wert: Optional[Decimal] = None
    """
    Der Modifikator in Prozent, der auf den Preis der referenzierten Preisposition angewendet wird.
    Der Wert wird multiplikativ angewendet. D.h. wenn bspw. ein Rabatt von 20% angewendet werden soll, muss der Wert
    `0,8` betragen.
    """
