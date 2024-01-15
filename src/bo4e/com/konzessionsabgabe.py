"""
Contains Konzessionsabgabe and corresponding marshmallow schema for de-/serialization
"""
from decimal import Decimal
from typing import Optional

from ..com.com import COM
from ..enum.abgabeart import AbgabeArt
from ..utils import postprocess_docstring

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Konzessionsabgabe(COM):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Konzessionsabgabe verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Konzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `Konzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Konzessionsabgabe.json>`_

    """

    #: Art der Abgabe
    satz: Optional[AbgabeArt] = None

    #: Konzessionsabgabe in E/kWh
    kosten: Optional[Decimal] = None

    #: Gebührenkategorie der Konzessionsabgabe
    kategorie: Optional[str] = None
