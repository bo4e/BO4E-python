"""
Contains Rufnummer class and corresponding marshmallow schema for de-/serialization
"""
from pydantic import StrictStr

from bo4e.com.com import COM
from bo4e.enum.rufnummernart import Rufnummernart


# pylint: disable=too-few-public-methods


class Rufnummer(COM):
    """
    Contains information to call or fax someone

    .. HINT::
        `Rufnummer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RufnummerSchema.json>`_

    """

    # required attributes
    #: Ausprägung der Nummer
    nummerntyp: Rufnummernart
    #: Die konkrete Nummer
    rufnummer: str
