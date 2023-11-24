"""
Contains Marktgebietinfo class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from .com import COM

# pylint: disable=too-few-public-methods


class MarktgebietInfo(COM):
    """
    Informationen zum Marktgebiet im Gas.

    .. raw:: html

        <object data="../_static/images/bo4e/com/MarktgebietInfo.svg" type="image/svg+xml"></object>

    .. HINT::
        `MarktgebietInfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/MarktgebietInfo.json>`_

    """

    marktgebiet: Optional[str] = None  #: Der Name des Marktgebietes
    marktgebietcode: Optional[str] = None  #: Die standardisierte Codenummer des Marktgebietes
