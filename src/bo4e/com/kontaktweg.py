"""
Contains Kontaktweg class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.kontaktart import Kontaktart


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Kontaktweg(COM):
    """
    Die Komponente wird dazu verwendet, die Kontaktwege innerhalb des BOs Person darzustellen

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kontakt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kontakt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Kontakt.json>`_

    """

    #: Gibt die Kontaktart des Kontaktes an.
    kontaktart: Optional["Kontaktart"] = None
    #: Spezifikation, beispielsweise "Durchwahl", "Sammelnummer" etc.
    beschreibung: Optional[str] = None
    #: Die Nummer oder E-Mail-Adresse.
    kontaktwert: Optional[str] = None
    #: Gibt an, ob es sich um den bevorzugten Kontaktweg handelt.
    ist_bevorzugter_kontaktweg: Optional[bool] = None
