"""
Contains Rufnummer class and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.rufnummernart import Rufnummernart

# pylint: disable=too-few-public-methods


class Rufnummer(COM):
    """
    Contains information to call or fax someone

    .. raw:: html

        <object data="../_static/images/bo4e/com/Rufnummer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Rufnummer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Rufnummer.json>`_

    """

    # required attributes
    #: Ausprägung der Nummer
    nummerntyp: Rufnummernart
    #: Die konkrete Nummer
    rufnummer: str
