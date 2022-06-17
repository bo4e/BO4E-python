"""
Contains Marktgebietinfo class
and corresponding marshmallow schema for de-/serialization
"""
from pydantic import StrictStr

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class MarktgebietInfo(COM):
    """
    Informationen zum Marktgebiet im Gas.

    .. HINT::
        `MarktgebietInfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/MarktgebietInfoSchema.json>`_

    """

    # required attributes
    marktgebiet: str  #: Der Name des Marktgebietes
    marktgebietcode: str  #: Die standardisierte Codenummer des Marktgebietes
