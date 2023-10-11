"""
Contains Dienstleistung class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.dienstleistungstyp import Dienstleistungstyp
from .com import COM

# pylint: disable=too-few-public-methods


class Dienstleistung(COM):
    """
    Abbildung einer abrechenbaren Dienstleistung.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Dienstleistung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Dienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Dienstleistung.json>`_

    """

    #: Kennzeichnung der Dienstleistung
    dienstleistungstyp: Optional[Dienstleistungstyp] = None
    #: Bezeichnung der Dienstleistung
    bezeichnung: Optional[str] = None
