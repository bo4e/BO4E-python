"""
Contains KriteriumWert class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

# pylint: disable=too-few-public-methods
from ..enum.tarifregionskriterium import Tarifregionskriterium
from .com import COM


class KriteriumWert(COM):
    """
    Mit dieser Komponente können Kriterien und deren Werte definiert werden

    .. raw:: html

        <object data="../_static/images/bo4e/com/KriteriumWert.svg" type="image/svg+xml"></object>

    .. HINT::
        `KriteriumWert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/KriteriumWert.json>`_

    """

    #: Hier steht, für welches Kriterium der Wert gilt. Z.B. Postleitzahlen
    kriterium: Optional[Tarifregionskriterium] = None
    #: Ein Wert, passend zum Kriterium. Z.B. eine Postleitzahl.
    wert: Optional[str] = None
