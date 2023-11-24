"""
Contains Tarifpreis class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.preistyp import Preistyp
from .preis import Preis

# pylint: disable=too-few-public-methods


class Tarifpreis(Preis):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Tarifpreis.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreis JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Tarifpreis.json>`_

    """

    #:  Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Optional[Preistyp] = None

    #:  Beschreibung des Preises. Hier können z.B. Preisdetails angegeben sein, beispielsweise "Drehstromzähler".
    beschreibung: Optional[str] = None
