"""
Contains Katasteradresse class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from .com import COM

# pylint: disable=too-few-public-methods


class Katasteradresse(COM):
    """
    Dient der Adressierung über die Liegenschafts-Information.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Katasteradresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Katasteradresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Katasteradresse.json>`_

    """

    gemarkung_flur: Optional[str] = None
    flurstueck: Optional[str] = None
