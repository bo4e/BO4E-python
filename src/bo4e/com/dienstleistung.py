"""
Contains Dienstleistung class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp


# pylint: disable=too-few-public-methods


class Dienstleistung(COM):
    """
    Abbildung einer abrechenbaren Dienstleistung.

    .. HINT::
        `Dienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/DienstleistungSchema.json>`_

    """

    # required attributes
    #: Kennzeichnung der Dienstleistung
    dienstleistungstyp: Dienstleistungstyp
    #: Bezeichnung der Dienstleistung
    bezeichnung: str
