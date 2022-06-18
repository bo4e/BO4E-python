"""
Contains Preisgarantie class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.preisgarantietyp import Preisgarantietyp


# pylint: disable=too-few-public-methods


class Preisgarantie(COM):
    """
    Definition für eine Preisgarantie mit der Möglichkeit verschiedener Ausprägungen.

    .. HINT::
        `Preisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/PreisgarantieSchema.json>`_

    """

    # required attributes
    #: Festlegung, auf welche Preisbestandteile die Garantie gewährt wird.
    preisgarantietyp: Preisgarantietyp
    zeitliche_gueltigkeit: Zeitraum
    """ Zeitraum, bis zu dem die Preisgarantie gilt, z.B. bis zu einem absolutem / fixem Datum
    oder als Laufzeit in Monaten. """

    # optionale attributes
    #: Freitext zur Beschreibung der Preisgarantie.
    beschreibung: str = None
