"""
Contains Rufnummer class and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.rufnummernart import Rufnummernart
from .com import COM

# pylint: disable=too-few-public-methods


class Rufnummer(COM):
    """
    Contains information to call or fax someone

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rufnummer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rufnummer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Rufnummer.json>`_

    """

    #: Ausprägung der Nummer
    nummerntyp: Optional[Rufnummernart] = None
    #: Die konkrete Nummer
    rufnummer: Optional[str] = None
