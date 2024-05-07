"""
Contains Tarifpreis class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .preis import Preis

if TYPE_CHECKING:
    from ..enum.preistyp import Preistyp


# pylint: disable=too-few-public-methods


@postprocess_docstring
class Tarifpreis(Preis):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Tarifpreis.json>`_

    """

    #:  Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Optional["Preistyp"] = None

    #:  Beschreibung des Preises. Hier können z.B. Preisdetails angegeben sein, beispielsweise "Drehstromzähler".
    beschreibung: Optional[str] = None
