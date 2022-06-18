"""
Contains KriteriumWert class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM

# pylint: disable=too-few-public-methods
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium


class KriteriumWert(COM):
    """
    Mit dieser Komponente können Kriterien und deren Werte definiert werden

    .. HINT::
        `KriteriumWert JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/KriteriumWertSchema.json>`_

    """

    # required attributes
    #: Hier steht, für welches Kriterium der Wert gilt. Z.B. Postleitzahlen
    kriterium: Tarifregionskriterium
    #: Ein Wert, passend zum Kriterium. Z.B. eine Postleitzahl.
    wert: str
